import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.delete("file-Mxv123sEdfnAknRoPEh1PQqkwMOwwReRc")
print(openai.File.list())