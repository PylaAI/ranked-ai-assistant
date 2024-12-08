import requests
from bs4 import BeautifulSoup
from typing import List, Optional
import re
from scrapper.types import BrawlerColData
from utils import colorful_print

class MapData:
    @staticmethod
    def map_data(url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tbody = soup.find(id='brawlersTableBody')

        if not tbody:
            raise LookupError("No tbody found.")

        return tbody

    def find_float(self, string: str) -> float or None:
        match = re.search(r'[\d.]+', string)
        if match:
            return float(match.group(0))

    def map_col_to_data(self, col: List[BeautifulSoup]) -> Optional[BrawlerColData]:
        if len(col) != 4:
            return None

        brawler_name = col[0].find('span').text
        winrate = self.find_float(col[1].text)
        pickrate = self.find_float(col[2].text)

        if not pickrate or not winrate:
            return None

        score = col[3].text

        return BrawlerColData(brawler_name, winrate, pickrate, float(score)).to_dict()
