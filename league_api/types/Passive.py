from league_api.api import ApiType
from typing import List, Mapping

from .Image import Image


class Passive(ApiType):
    image: Image = None
    sanitizedDescription: str = None
    name: str = None
    description: str = None

    @property
    def sanitized_description(self):
        return self.sanitizedDescription

    @sanitized_description.setter
    def sanitized_description(self, value):
        self.sanitizedDescription = value

