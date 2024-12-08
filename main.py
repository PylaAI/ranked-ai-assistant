from openai import OpenAI
from context import CONTEXT
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": CONTEXT},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
)

print(str(completion.choices[0].message.content))