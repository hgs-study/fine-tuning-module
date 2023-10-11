import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# create model
openai.FineTuningJob.delete()

# get list
print(openai.FineTuningJob.list(limit=10))
