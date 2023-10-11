import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.FineTuningJob.list_events(id="ftjob-Gd197C5gas90aoCans020ma8HJjsmffkmn", limit=10))