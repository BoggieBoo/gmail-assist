from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
def ask_gpt(text):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
    messages=[{"role": "user", "content": text}],model="gpt-4",)
    return response.choices[0].message.content

# test
print("Response text: " + ask_gpt("hello"))

