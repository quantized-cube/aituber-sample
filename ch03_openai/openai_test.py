import os

from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "あなたは端的に発言するAIです。"},
    {"role": "user", "content": "こんにちは。"},
]

res = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
print(res)
print(res.choices[0].message.content)
