from league_api.client import Client
import sys

api_key = sys.argv[1]
c = Client(api_key, 'na1')
print(c.get_champion_list(dataById=True))
