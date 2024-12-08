from scrapper.types import PrintColors
from typing import Union

def value_to_URL_value(val: str):
    return "-".join(val.lower().split(' '))


def colorful_print(text: str, color: PrintColors):
    print(f"\033[{color}m{text}\033[0m")


def find_closest_number_key(data: any, number: Union[int, float]):
    return min(data.keys(), key=lambda k: abs(k - number))
