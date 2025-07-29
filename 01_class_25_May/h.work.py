#from ky bad """Ye custome library ya module khlata hy"""
#import ky bad """Ye classes khaylati hain"""

from agents import Agent
from agents import RunConfig
from agents import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
from agents import Runner

load_dotenv() 
'''When you call load_dotenv(), it reads the .env file and adds the variables to your environment
it is used to load environment varaibles from dotenv'''


gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", #Google ki API KA URL
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  #Google ki api gemini ka free model
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

translator = Agent(
    name = 'Translator Agent',
    instructions= 'You are a Translator Agent . You will translate any lanuage into english lanuage'

)

response = Runner.run_sync(
    translator,
    input='میں اپنی زندگی میں کامیاب ہونا چاہتا ہوں۔',
    run_config=config
)
print(response)




