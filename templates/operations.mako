from .api import api_function
from .types import *
from typing import List, Mapping

% for op in operations:
${op['name']} = api_function(${repr(op['path'])}, ${op['type']}\
%   for param in op['path_params']:
, ${param['type']}\
%   endfor
%   for param in op['query_params']:
, ${param['name']}=${param['type']}\
%   endfor
)
% endfor