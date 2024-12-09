from openai import OpenAI
from context import CONTEXT
from scrapper.Validator import main as validator_main
from scrapper.utils import colorful_print
from scrapper.types import PrintColors

api_key = "333"
client = OpenAI(api_key=api_key)

brawlers_data = validator_main()
ally_brawlers = "frank, poco"
enemy_brawlers = "piper"

USER_INPUT = (f"brawlers_data: {brawlers_data}, "
              f"ally_brawlers: [{ally_brawlers}], "
              f"enemy_players: [{enemy_brawlers}], "
              f"map: Hideout (bounty)")


def PYLA_AI():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": CONTEXT},
            {"role": "user", "content": USER_INPUT}
        ]
    )
    return completion.choices[0].message


response = PYLA_AI()

colorful_print(str(response.content), PrintColors.Blue)
colorful_print("MONEY SPENT: ", PrintColors.Red)
colorful_print(f"{len(CONTEXT + USER_INPUT + response.content) * (3 / 1000000)}$",
               PrintColors.Yellow)
