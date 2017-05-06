from league_api.api import ApiType
from typing import List, Mapping



class Observer(ApiType):
    encryptionKey: str = None  # Key used to decrypt the spectator grid game data for playback

    @property
    def encryption_key(self):
        return self.encryptionKey

    @encryption_key.setter
    def encryption_key(self, value):
        self.encryptionKey = value

