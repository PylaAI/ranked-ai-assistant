
from scrapper.Scrapper import Scrapper
from scrapper.types import GameModes
import json
from scrapper.utils import value_to_URL_value

scrapper = Scrapper()
gamemode_maps = scrapper.get_gamemode_maps(gamemode_type=GameModes.Any)
result = scrapper.get_maps_data(gamemode_maps)


with open('data.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

