import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:fine-tuning-practice-test:4slkn8s2dff6cT2ai0",
  messages=[
    {"role": "system", "content": "책을 요약해줘"},
    {"role": "user", "content": "빨간머리 앤 소녀의 이야기입니다. 빨간머리앤은 착합니다. 아동입니다."}
  ]
)
message=completion.choices[0].message
print(message.role)
print(message.content)