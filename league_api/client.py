from . import operations
from .api import Context


class Client(Context):
    pass

# TODO:
# Caching
# Rate limiting - This should be straightforward; use semaphores and coroutines to release them
for name, func in operations.__dict__.items():
    if not getattr(func, '_is_api_func', False):
        continue
    setattr(Client, name, func)