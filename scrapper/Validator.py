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
from scrapper.types import BrawlerColData
from scrapper.utils import find_closest_number_key
from typing import List, Union
from scrapper.types import ConfResult


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

    def validate(self, map_data: List[BrawlerColData]) -> List[ConfResult]:
        result = []
        for col in map_data:
            data_conf = self.data_confidence(col, map_data)
            result.append(ConfResult(col, data_conf, col.name))

        return sorted(result, key=lambda x: x.conf, reverse=True)[:15]

    def data_confidence(self, col_data: BrawlerColData, map_data: List[BrawlerColData]):
        validators_result = sum([
            self.__winrate(col_data.winrate),
            self.__score(col_data, map_data),
            self.__pickrate(col_data.pickrate)
        ])

        return 10 - validators_result

    def __winrate(self, winrate: float) -> Union[int, float]:
        punishment_key = find_closest_number_key(self.winrate_punishments, winrate)
        return self.winrate_punishments[punishment_key]

    def __score(self, col: BrawlerColData, map_data: List[BrawlerColData]) -> Union[int | float]:
        sorted_map_data = sorted(map_data, key=lambda x: x.score)
        brawler_placement = sorted_map_data.index(col)
        punishment_key = find_closest_number_key(self.score_punishments, brawler_placement)
        return self.score_punishments[punishment_key]

    def __pickrate(self, pickrate: float) -> Union[int | float]:
        punishment_key = find_closest_number_key(self.pickrate_punishments, pickrate)
        return self.pickrate_punishments[punishment_key]


map_data = [
    {
        "name": "Stu",
        "winrate": 54.0,
        "pickrate": 6.86,
        "score": 169.6
    },
    {
        "name": "Mortis",
        "winrate": 27.2,
        "pickrate": 7.66,
        "score": 169.5
    },
    {
        "name": "Piper",
        "winrate": 67.1,
        "pickrate": 5.21,
        "score": 144.5
    },
    {
        "name": "Colt",
        "winrate": 39.8,
        "pickrate": 5.34,
        "score": 130.7
    },
    {
        "name": "Bea",
        "winrate": 65.7,
        "pickrate": 3.39,
        "score": 107.2
    },
    {
        "name": "Max",
        "winrate": 57.9,
        "pickrate": 3.05,
        "score": 95.8
    },
    {
        "name": "Byron",
        "winrate": 66.0,
        "pickrate": 2.65,
        "score": 92.6
    },
    {
        "name": "Moe",
        "winrate": 54.4,
        "pickrate": 2.92,
        "score": 91.0
    },
    {
        "name": "Leon",
        "winrate": 67.8,
        "pickrate": 2.45,
        "score": 89.7
    },
    {
        "name": "Belle",
        "winrate": 75.2,
        "pickrate": 2.17,
        "score": 88.5
    },
    {
        "name": "Gus",
        "winrate": 69.9,
        "pickrate": 2.08,
        "score": 83.5
    },
    {
        "name": "Fang",
        "winrate": 41.6,
        "pickrate": 2.81,
        "score": 81.1
    },
    {
        "name": "Melodie",
        "winrate": 53.4,
        "pickrate": 2.32,
        "score": 78.5
    },
    {
        "name": "Surge",
        "winrate": 25.5,
        "pickrate": 3.09,
        "score": 77.1
    },
    {
        "name": "Pearl",
        "winrate": 78.1,
        "pickrate": 1.36,
        "score": 74.1
    },
    {
        "name": "Lola",
        "winrate": 80.5,
        "pickrate": 1.22,
        "score": 72.7
    },
    {
        "name": "Carl",
        "winrate": 65.4,
        "pickrate": 1.58,
        "score": 70.9
    },
    {
        "name": "Pam",
        "winrate": 85.7,
        "pickrate": 0.97,
        "score": 70.8
    },
    {
        "name": "Clancy",
        "winrate": 39.6,
        "pickrate": 2.34,
        "score": 70.5
    },
    {
        "name": "Nani",
        "winrate": 76.9,
        "pickrate": 1.21,
        "score": 70.3
    },
    {
        "name": "Kenji",
        "winrate": 31.7,
        "pickrate": 2.42,
        "score": 67.4
    },
    {
        "name": "Bo",
        "winrate": 71.4,
        "pickrate": 1.21,
        "score": 67.1
    },
    {
        "name": "Amber",
        "winrate": 70.2,
        "pickrate": 1.19,
        "score": 65.9
    },
    {
        "name": "Penny",
        "winrate": 75.1,
        "pickrate": 1.03,
        "score": 65.7
    },
    {
        "name": "Otis",
        "winrate": 70.1,
        "pickrate": 1.06,
        "score": 63.3
    },
    {
        "name": "Spike",
        "winrate": 56.0,
        "pickrate": 1.46,
        "score": 62.8
    },
    {
        "name": "Frank",
        "winrate": 20.8,
        "pickrate": 2.51,
        "score": 62.7
    },
    {
        "name": "Crow",
        "winrate": 47.3,
        "pickrate": 1.7,
        "score": 62.4
    },
    {
        "name": "Mico",
        "winrate": 89.8,
        "pickrate": 0.3,
        "score": 59.9
    },
    {
        "name": "Colette",
        "winrate": 53.9,
        "pickrate": 1.34,
        "score": 59.2
    },
    {
        "name": "Angelo",
        "winrate": 81.1,
        "pickrate": 0.49,
        "score": 58.5
    },
    {
        "name": "Brock",
        "winrate": 61.5,
        "pickrate": 0.94,
        "score": 55.7
    },
    {
        "name": "Rico",
        "winrate": 20.7,
        "pickrate": 2.12,
        "score": 54.8
    },
    {
        "name": "8-Bit",
        "winrate": 68.8,
        "pickrate": 0.67,
        "score": 54.7
    },
    {
        "name": "Chester",
        "winrate": 61.2,
        "pickrate": 0.88,
        "score": 54.3
    },
    {
        "name": "Mr. P",
        "winrate": 81.7,
        "pickrate": 0.26,
        "score": 54.2
    },
    {
        "name": "Shade",
        "winrate": 86.5,
        "pickrate": 0.1,
        "score": 53.9
    },
    {
        "name": "Bonnie",
        "winrate": 70.9,
        "pickrate": 0.56,
        "score": 53.8
    },
    {
        "name": "Lou",
        "winrate": 64.7,
        "pickrate": 0.74,
        "score": 53.6
    },
    {
        "name": "Ash",
        "winrate": 82.9,
        "pickrate": 0.19,
        "score": 53.5
    },
    {
        "name": "Gale",
        "winrate": 37.7,
        "pickrate": 1.45,
        "score": 51.6
    },
    {
        "name": "Janet",
        "winrate": 77.1,
        "pickrate": 0.17,
        "score": 49.6
    },
    {
        "name": "Bibi",
        "winrate": 17.6,
        "pickrate": 1.94,
        "score": 49.4
    },
    {
        "name": "Charlie",
        "winrate": 70.9,
        "pickrate": 0.31,
        "score": 48.8
    },
    {
        "name": "Juju",
        "winrate": 66.2,
        "pickrate": 0.44,
        "score": 48.5
    },
    {
        "name": "Maisie",
        "winrate": 44.9,
        "pickrate": 1.06,
        "score": 48.2
    },
    {
        "name": "Meg",
        "winrate": 52.0,
        "pickrate": 0.78,
        "score": 46.8
    },
    {
        "name": "Darryl",
        "winrate": 41.5,
        "pickrate": 1.09,
        "score": 46.7
    },
    {
        "name": "Gray",
        "winrate": 61.5,
        "pickrate": 0.47,
        "score": 46.3
    },
    {
        "name": "R-T",
        "winrate": 63.3,
        "pickrate": 0.3,
        "score": 44.0
    },
    {
        "name": "Eve",
        "winrate": 70.0,
        "pickrate": 0.06,
        "score": 43.2
    },
    {
        "name": "Kit",
        "winrate": 56.9,
        "pickrate": 0.42,
        "score": 42.5
    },
    {
        "name": "Griff",
        "winrate": 50.0,
        "pickrate": 0.58,
        "score": 41.6
    },
    {
        "name": "Squeak",
        "winrate": 58.1,
        "pickrate": 0.24,
        "score": 39.7
    },
    {
        "name": "Ruffs",
        "winrate": 57.1,
        "pickrate": 0.23,
        "score": 38.9
    },
    {
        "name": "Chuck",
        "winrate": 62.5,
        "pickrate": 0.02,
        "score": 37.9
    },
    {
        "name": "Larry & Lawrie",
        "winrate": 55.9,
        "pickrate": 0.09,
        "score": 35.3
    },
    {
        "name": "Buzz",
        "winrate": 15.7,
        "pickrate": 1.15,
        "score": 32.4
    },
    {
        "name": "Tara",
        "winrate": 31.9,
        "pickrate": 0.65,
        "score": 32.2
    },
    {
        "name": "Poco",
        "winrate": 39.6,
        "pickrate": 0.4,
        "score": 31.8
    },
    {
        "name": "Mandy",
        "winrate": 45.2,
        "pickrate": 0.2,
        "score": 31.1
    },
    {
        "name": "Draco",
        "winrate": 47.1,
        "pickrate": 0.09,
        "score": 30.0
    },
    {
        "name": "El Primo",
        "winrate": 30.5,
        "pickrate": 0.55,
        "score": 29.3
    },
    {
        "name": "Hank",
        "winrate": 43.6,
        "pickrate": 0.11,
        "score": 28.4
    },
    {
        "name": "Gene",
        "winrate": 40.9,
        "pickrate": 0.18,
        "score": 28.2
    },
    {
        "name": "Sprout",
        "winrate": 45.5,
        "pickrate": 0.03,
        "score": 27.9
    },
    {
        "name": "Jessie",
        "winrate": 32.1,
        "pickrate": 0.43,
        "score": 27.8
    },
    {
        "name": "Lily",
        "winrate": 37.9,
        "pickrate": 0.16,
        "score": 26.0
    },
    {
        "name": "Sam",
        "winrate": 38.5,
        "pickrate": 0.07,
        "score": 24.5
    },
    {
        "name": "Berry",
        "winrate": 38.9,
        "pickrate": 0.05,
        "score": 24.3
    },
    {
        "name": "Jacky",
        "winrate": 13.0,
        "pickrate": 0.77,
        "score": 23.2
    },
    {
        "name": "Buster",
        "winrate": 32.8,
        "pickrate": 0.16,
        "score": 22.9
    },
    {
        "name": "Edgar",
        "winrate": 12.7,
        "pickrate": 0.72,
        "score": 22.0
    },
    {
        "name": "Shelly",
        "winrate": 20.2,
        "pickrate": 0.49,
        "score": 21.9
    },
    {
        "name": "Dynamike",
        "winrate": 13.8,
        "pickrate": 0.67,
        "score": 21.7
    },
    {
        "name": "Bull",
        "winrate": 28.8,
        "pickrate": 0.22,
        "score": 21.7
    },
    {
        "name": "Grom",
        "winrate": 33.3,
        "pickrate": 0.02,
        "score": 20.4
    },
    {
        "name": "Emz",
        "winrate": 24.0,
        "pickrate": 0.28,
        "score": 20.0
    },
    {
        "name": "Doug",
        "winrate": 29.4,
        "pickrate": 0.05,
        "score": 18.7
    },
    {
        "name": "Nita",
        "winrate": 14.8,
        "pickrate": 0.3,
        "score": 14.9
    },
    {
        "name": "Cordelius",
        "winrate": 17.7,
        "pickrate": 0.19,
        "score": 14.4
    },
    {
        "name": "Barley",
        "winrate": 20.0,
        "pickrate": 0.03,
        "score": 12.6
    },
    {
        "name": "Tick",
        "winrate": 5.5,
        "pickrate": 0.25,
        "score": 8.3
    },
    {
        "name": "Sandy",
        "winrate": 5.3,
        "pickrate": 0.21,
        "score": 7.4
    },
    {
        "name": "Willow",
        "winrate": 6.7,
        "pickrate": 0.04,
        "score": 4.8
    },
]


def main():
    res = []
    for data in map_data:
        res.append(BrawlerColData(**data))

    validator = Validator()
    validated_data = validator.validate(res)

    reduced_data = []

    for c in validated_data:
        reduced_data.append(f"{c.brawler_name}, {c.data.winrate}, {c.data.pickrate}, {c.conf}")

    return reduced_data
