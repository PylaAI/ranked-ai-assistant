"""
Start with 10 points

Firstly factor in score. Only pick top 15 brawlers.

Punishments:
- Easily unlockable brawlers -> - 3-5 points
: Highly picked brawlers on avarage are played mostly in lower trophies. Which
makes the data incorrect for higher ladder.

- High winrate -> >90% => -5; >80% => -3; >70% => -2
: Such high winrates are only possible by pro players who pick the less picked brawlers.
Them playing the brawler for a whole day can completely influence the winrate.

- Brawler with very low play rate -> < top 10 => -3; top 20 => -2
: Low pickrate => brawler is not good / good only in the right conditions

Pros:
- High winrate + high pickrate => + 1-5 points
- Perfect for specific map => + 1-5 points
- Good with team combo => + 1-5 points
- Good against enemy combo => + 1-5 points
"""
from typing import List, Union
from scrapper.types import BrawlerColData
from scrapper.utils import find_closest_number_key


class Validator:

    def __init__(self):
        self.empty = None
        self.winrate_punishments = {
            90: 5,
            80: 3,
            70: 2,
            65: -2,
            60: 1,
            55: 1,
            54: 0,
            45: 0,
            40: 2,
            30: 4
        }

        # place from first to last
        self.score_punishments = {
            20: 10,
            17: 5,
            15: 0,
            10: 0,
            8: -1,  # add instead of punish
            5: -2,
            3: -2,
            1: -3

        }
        self.pickrate_punishments = {
            10: -5,
            8.1: -5,
            8: -3,
            5: -2,
            3: -1,
            2: 0,
            1: 0,
            0.5: 2,
            0.25: 4,
            0: 10
        }

    def validate(self, map_data: List[BrawlerColData]):
        result = {}
        for col in map_data:
            data_conf = self.data_confidence(col, map_data)
            result[col.name] = {**map_data, 'conf': data_conf}

        return result

    def data_confidence(self, col_data: BrawlerColData, map_data: List[BrawlerColData]):
        validators_result = sum([
            self.__winrate(col_data.winrate),
            self.__score(col_data, map_data),
            self.__pickrate(col_data.pickrate)
        ])

        return 10 - validators_result

    def __winrate(self, winrate: float) -> Union[int | float]:
        punishment_key = find_closest_number_key(self.winrate_punishments, winrate)
        return self.winrate_punishments[punishment_key]

    def __score(self, col: BrawlerColData, map_data: List[BrawlerColData]) -> Union[int | float]:
        sorted_map_data = sorted(map_data, key=lambda x: x['score'])
        brawler_placement = sorted_map_data.index(col)
        punishment_key = find_closest_number_key(self.score_punishments, brawler_placement)
        return self.score_punishments[punishment_key]

    def __pickrate(self, pickrate: float) -> Union[int | float]:
        punishment_key = find_closest_number_key(self.pickrate_punishments, pickrate)
        return self.pickrate_punishments[punishment_key]
