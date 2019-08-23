import re

import json
import scrapy

from scrapy.utils.serialize import ScrapyJSONEncoder
_encoder = ScrapyJSONEncoder()


class Operation(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    method = scrapy.Field()
    path = scrapy.Field()
    path_params = scrapy.Field()
    query_params = scrapy.Field()


class Field(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    doc = scrapy.Field()


class Type(scrapy.Item):
    name = scrapy.Field()
    fields = scrapy.Field()


def snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

un_dto_pattern = re.compile('dto', re.IGNORECASE)


def un_dto(string):
    return un_dto_pattern.sub('', string)


def sanitize_type(string):
    string = un_dto(string)
    string = re.sub(r'\blong\b', 'int', string)
    string = re.sub(r'\bLong\b', 'int', string)
    string = re.sub(r'\bdouble\b', 'float', string)
    string = re.sub(r'\bboolean\b', 'bool', string)
    string = re.sub(r'\bMap\b', 'Mapping', string)
    string = re.sub(r'\bSet\b', 'List', string)
    string = re.sub(r'\bstring\b', 'str', string)
    string = re.sub(r'\bString\b', 'str', string)
    return string


class JsonWriterPipeline(object):
    types = {}
    operations = {}

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        file = open('api.json', 'w')
        file.write(_encoder.encode({'types': self.types, 'operations': self.operations}))

    def process_item(self, item, spider):
        if isinstance(item, Type):
            if item['name'] not in self.types:
                self.types[item['name']] = item
            else:
                print(item['name'])
                fields = self.types[item['name']]['fields']
                names = [field['name'] for field in fields]
                for field in item['fields']:
                    if field['name'] not in names:
                        fields.append(field)
        if isinstance(item, Operation):
            self.operations[item['name']] = item
        return item


class APIScraper(scrapy.Spider):
    name = 'apis'
    start_urls = ['https://developer.riotgames.com/api-methods/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'api_scraper.JsonWriterPipeline': 800,
        }
    }

    def parse(self, response):
        for name in response.css('li:contains("Standard APIs") a.api_option::attr("api-name")').extract():
            if not name.endswith('-v3') and not name.endswith('-v4'):
                continue

            url = 'https://developer.riotgames.com/api-details/' + name
            yield scrapy.Request(url=url, callback=self.parse_api)

    def parse_api(self, response):
        response = response.replace(body=json.loads(response.text)['html'])
        for list_item in response.css('ul.operations li.operation'):
            name = snake(list_item.css('::attr("id")').extract_first()[1:]).strip()
            method = list_item.css('span.http_method a::text').extract_first().strip()
            path = list_item.css('span.path a::text').extract_first().strip()

            outputs = list_item.css('div.api_block:contains("Return value: ")')
            type = sanitize_type(outputs.css('div.response_body h4::text').extract_first().replace("Return value: ", '').strip())
            outputs = list_item.css('div.api_block:contains("Return value: ") div.response_body')[1:]
            for output in outputs:
                yield self.parse_type(output)
            path_params = [self.parse_param(row) for row in
                           list_item.css('div.api_block:contains("Path Parameters") tbody.operation-params tr')]
            query_params = [self.parse_param(row) for row in
                           list_item.css('div.api_block:contains("Query Parameters") tbody.operation-params tr')]
            yield Operation(name=name, method=method, path=path, type=type, path_params=path_params, query_params=query_params)

    def parse_type(self, output):
        name = un_dto(output.css('h5::text').extract_first()).strip()
        rows = output.css('table tbody tr')
        fields = []
        value = Type(name=name, fields=fields)
        for row in rows:
            name, type, doc = row.css('td::text').extract()
            name = name
            type = sanitize_type(type)
            doc = doc.strip()
            fields.append(Field(name=name, type=type, doc=doc))
        return value

    def parse_param(self, row):
        name, *dummy, doc = row.css('td::text').extract()
        name = name.strip()
        doc = doc.strip()
        type = sanitize_type(row.css('span.model-signature::text').extract_first().strip())
        return Field(name=name, type=type, doc=doc)
