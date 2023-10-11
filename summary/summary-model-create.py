import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# create new model 
openai.FineTuningJob.create(training_file="file-Mxv123sEdfnAknRoPEh1PQqkwMOwwReRc", model="gpt-3.5-turbo", suffix="fine-tuning-practice-test")

# already created model
#openai.FineTuningJob.create(training_file="file-Mxv123sEdfnAknRoPEh1PQqkwMOwwReRc", model="ft:gpt-3.5-turbo-0613:fine-tuning-practice-test::4slkn8s2dff6cT2ai0", suffix="fine-tuning-practice-test")

# get list
print(openai.FineTuningJob.list(limit=10))
