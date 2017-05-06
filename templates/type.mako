from league_api.api import ApiType
from typing import List, Mapping

% for dependency in type['deps']:
from .${dependency} import ${dependency}
% endfor


class ${type['name']}(ApiType):
% for field in type['fields']:
<% if iskeyword(field['name']): field['name'] = '_' + field['name'] %>\
%   if field['name'] != 'from':
    ${field['name']}: ${field['type']} = None${'  # ' + field['doc'] if field['doc'] else ''}
%   endif
% endfor

% for field in type['fields']:
<%
    name = field['name']
    snaked = snake(name)
%>\
%   if name != snaked:
    @property
    def ${snaked}(self):
        return self.${name}

    @${snaked}.setter
    def ${snaked}(self, value):
        self.${name} = value

%   endif
% endfor
