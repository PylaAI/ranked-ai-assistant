from typing import List, Dict, Union


class BrawlerColData:
    def __init__(self, name: str, winrate: float, pickrate: float, score: float):
        self.name = name
        self.winrate = winrate
        self.pickrate = pickrate
        self.score = score

    def __str__(self):
        return f"Name: {self.name} \nwinrate: {self.winrate} \npickrate: {self.pickrate} \nscore: {self.score}"

    def to_dict(self):
        return {
            "name": self.name,
            "winrate": self.winrate,
            "pickrate": self.pickrate,
            "score": self.score
        }


class MapsDataResult:
    result: Dict[str, List['BrawlerColData']] = {}
    errors: List[str] = []


class GameModes:
    Showdown = "showdown"
    GemGrab = "gem grab"
    Heist = "heist"
    HotZone = "hot zone"
    Knockout = "knockout"
    Bounty = "bounty"
    Any = "any"


class PrintColors:
    Red = '31'
    Green = '32'
    Yellow = '33'
    Blue = '34'


class ConfResult:
    def __init__(self, data: BrawlerColData, conf: Union[float, int], brawler_name: str):
        self.data = data
        self.conf = conf
        self.brawler_name = brawler_name


