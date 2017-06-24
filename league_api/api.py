from typing import Mapping, List

import aiohttp
import requests
from keyword import iskeyword


class Context:
    def __init__(self, api_key, region, client):
        self.api_key = api_key
        self.region = region
        self.client = client

    def get(self, path, **kwargs):
        kwargs['api_key'] = self.api_key
        url = "https://{}.api.riotgames.com/{}".format(self.region, path)
        return self.client.get(url, params=kwargs)


class ApiType:
    def __init__(self, dict):
        for name in dict.keys():
            if iskeyword(name):
                name = '_' + name
            if name not in self.__annotations__:
                continue
            type = self.__annotations__[name]
            if issubclass(type, ApiType):
                setattr(self, name, type(dict[name]))
            elif issubclass(type, Mapping):
                t = type.__args__[1]
                if issubclass(t, ApiType):
                    values = {}
                    for key, value in dict[name].items():
                        values[key] = t(value)
                    setattr(self, name, values)
                else:
                    setattr(self, name, dict[name])
            elif issubclass(type, List):
                t = type.__args__[0]
                if issubclass(t, ApiType):
                    values = [t(i) for i in dict[name]]
                    setattr(self, name, values)
                else:
                    setattr(self, name, dict[name])
            else:
                setattr(self, name, dict[name])

    def __repr__(self):
        return repr(self.__dict__)


def convert(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'


def api_function(path: str, type, *required, **optional):
    async def __inner__(*args, **kwargs):
        if len(args) > 0 and isinstance(args[0], Context):
            context = args[0]
            args = args[1:]
        elif 'context' in kwargs:
            context = kwargs.pop('context')
        elif 'api_key' in kwargs:
            context = Context(kwargs.pop('api_key'), kwargs.pop('region', 'na1'))
        else:
            raise TypeError("must have a context")
        if len(args) != len(required):
            raise TypeError("takes exactly {} argument ({} given)".format(len(required), len(args)))
        resolved_path = path.format(*args)
        options = {k: convert(v) for k, v in kwargs.items() if k in optional}
        async with context.get(resolved_path, **options) as response:
            response.raise_for_status()  # throw an exception on bad response
            json = await response.json()
            if issubclass(type, Mapping):
                t = type.__args__[1]
                return {k: t(v) for k, v in json.items()}
            elif issubclass(type, List):
                t = type.__args__[0]
                return [t(i) for i in json]
            return type(json)

    __inner__._is_api_func = True
    return __inner__
