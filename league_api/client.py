from . import operations
from .api import Context


class Client(Context):
    pass

# TODO:
# Caching
# Rate limiting
for name, func in operations.__dict__.items():
    if not getattr(func, '_is_api_func', False):
        continue
    setattr(Client, name, func)