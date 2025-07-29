'''We started study from it's Sir Zia
https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first'''

'''Our class repo from Sir Ali Jawwad
https://github.com/jawwad-ali/Sunday_Afternoon_Agentic_AI'''

# pip install openai-agents #Ye openAi agents ky framework ko hmary projects ko install krdega terminal par chllyga
# pip install python-dotenv #env ka pkg install krna hay terminal par chllyga
from dotenv import load_dotenv 
from agents import Agent
from agents import OpenAIChatCompletionsModel # specific model configuration (OpenAI ke chat models ke liye).
from agents import RunConfig  # Configuration object jo agent ko chalane mein help karta hai.
from agents import AsyncOpenAI # Async (asynchronous) tarike se OpenAI se interact karne ke liye class.
import os
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

#Creating Agent 
'''Agents are defined with instructions, a name, and optional config'''
writer = Agent(
    name = 'Writer Agent',
    instructions= 'you are a writer agent. Generate poem, novel , stories, content , email etc'

)
###################################53 minutes lectures has SEEN
#Now executing agent
# runner agent ko execute krty hain
response = Runner.run_sync(
    writer, 
    input='Write a 2 paragraph essay on Generative AI.',
    run_config = config
    )
print(response)

