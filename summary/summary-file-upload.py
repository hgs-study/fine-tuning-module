import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
file= open("dataset/summary-dataset.jsonl", "rb")

openai.File.create(
  file=file,
  purpose='fine-tune',
  user_provided_filename= file.name
)

print(openai.File.list())
