from mako.template import Template
import json
import re
from operator import itemgetter
from keyword import iskeyword

pattern = re.compile(r'\w+')


def snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

utils = {'snake': snake, 'iskeyword': iskeyword}

if __name__ == '__main__':
    data = json.load(open('api.json'))
    types = sorted(data['types'].values(), key=itemgetter('name'))
    operations = sorted(data['operations'].values(), key=itemgetter('name'))
    for operation in operations:
        operation['path'] = re.sub(r'\{[^}]*}', '{}', operation['path'])

    template = Template(filename='templates/type.mako')

    for type in types:
        name = type['name']
        deps = {j for i in type['fields'] for j in pattern.findall(i['type'])}
        deps -= {'int', 'str', 'bool', 'float', 'object', 'List', 'Mapping'}
        type['deps'] = sorted(deps)
        print(deps)
        out = open('league_api/types/{}.py'.format(name), 'w')
        out.write(template.render(type=type, **utils))

    template = Template(filename='templates/types_init.mako')
    out = open('league_api/types/__init__.py', 'w')
    out.write(template.render(types=types, **utils))

    template = Template(filename='templates/operations.mako')
    out = open('league_api/operations.py', 'w')
    out.write(template.render(operations=operations, **utils))
