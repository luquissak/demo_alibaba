import os
import dashscope
from openai import OpenAI

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

messages = [
    {'role': 'system', 'content': 'Você é um assistente útil.'},
    {'role': 'user', 'content': 'Explique o que é o modelo Qwen em 2 frases.'}
]
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)

resp = client.chat.completions.create(
    model="qwen-plus",
    messages=messages
)

print(resp.choices[0].message.content)
