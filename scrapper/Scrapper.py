from MapData import MapData
import requests
from bs4 import BeautifulSoup
from typing import List
from scrapper.types import *
from utils import value_to_URL_value, colorful_print


class GameModeResult:
    def __init__(self, type: str, maps: List[str]):
        self.type = type
        self.maps = maps


class Scrapper:
    def __init__(self, debug=True):
        self.MapData = MapData()
        self.main_maps_URL = "https://www.noff.gg/brawl-stars/maps"
        self.base_map_URL = "https://www.noff.gg/brawl-stars/map/"
        self.debug = debug

    def __get_gamemodes(self) -> List[GameModeResult]:
        response = requests.get(self.main_maps_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        gamemode_maps = soup.find_all(class_="maps-mode")
        res: List[GameModeResult] = []

        for data in gamemode_maps:
            mode_heading: BeautifulSoup = data.find_all(class_="mode-heading")[0]
            gamemode_type = mode_heading.find('h2').text.lower()
            maps = list(map(lambda a_element: a_element.text, data.find_all('a')))

            res.append(GameModeResult(gamemode_type, maps))

        return res

    def get_map_data(self, map_name: str):
        tbody = MapData.map_data(self.base_map_URL + map_name)
        row = tbody.find_all('tr')
        return list(map(lambda col: self.MapData.map_col_to_data(col.find_all('td')), row))

    def get_gamemode_maps(self, gamemode_type: str) -> List[str]:
        gamemodes = self.__get_gamemodes()
        res = []

        for gamemode in gamemodes:
            if gamemode.type != gamemode_type and gamemode.type != GameModes.Any:
                res.extend(gamemode.maps)

        return res

    def __get_maps_data(self, gamemode_maps: List[str]):
        result = MapsDataResult()

        for map_name in gamemode_maps:
            try:
                map_data = self.get_map_data(value_to_URL_value(map_name))
                result.result[map_name] = map_data
                colorful_print(f"✓ {map_name}", PrintColors.Green)
            except LookupError as e:
                result.errors.append(f"Failed lookup on map with name {map_name}. Error: {e}")
            except Exception as e:
                result.errors.append(f"Unhandeled error for map with name {map_name}: {e}")

        return result

    def get_maps_data(self, gamemode_maps: List[str]):
        result = self.__get_maps_data(gamemode_maps)

        if self.debug and result.errors:
            colorful_print(f"Extracted data for {len(result.result)} maps.", PrintColors.Green)
            for err_message in result.errors:
                colorful_print(err_message, PrintColors.Red)

        return result.result
