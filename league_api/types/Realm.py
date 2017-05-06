from league_api.api import ApiType
from typing import List, Mapping



class Realm(ApiType):
    lg: str = None  # Legacy script mode for IE6 or older.
    dd: str = None  # Latest changed version of Dragon Magic.
    l: str = None  # Default language for this realm.
    n: Mapping[str, str] = None  # Latest changed version for each data type listed.
    profileiconmax: int = None  # Special behavior number identifying the largest profileicon id that can be used under 500. Any profileicon that is requested between this number and 500 should be mapped to 0.
    store: str = None  # Additional api data drawn from other sources that may be related to data dragon functionality.
    v: str = None  # Current version of this file for this realm.
    cdn: str = None  # The base CDN url.
    css: str = None  # Latest changed version of Dragon Magic's css file.

