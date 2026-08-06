# import os
# from dotenv import load_dotenv
# from groq import Groq

# # Load variables from .env
# load_dotenv()

# # Read API key
# my_api_key = os.getenv("GROQ_API_KEY")

# # Check API key
# if not my_api_key:
#     raise ValueError("WHERE IS MY API KEY?")

# # Create Groq client
# client = Groq(api_key=my_api_key)

# # Model name
# model = "llama-3.3-70b-versatile"


# def llm_ans(prompt):
#     message = {
#         #ROLE:
#         You are a support assistant at laptop/mobile company
        
#         "role": "user",
#         "content": prompt
#     }

#     messages = [message]

#     response = client.chat.completions.create(
#         model=model,
#         messages=messages
#     )

#     ans = response.choices[0].message.content
#     return ans


# # Bad Prompt
# bad_prompt = """
# This is a user complaint:
# My laptop is not working.
# Classify this.
# """

# print(llm_ans(bad_prompt))

import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"


def llm_ans(prompt):
    message={
        "role":"user",
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans


bad_prompt="""
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK: 
You have to classify the  issue in a category
#CONSTRAINT
You have to classify  the issue in one of  three categories  namely blining, technical, return
#output format
# Answer must be one word
#EXAMPLE 
for instance if user not happy our services or he says he wants to refund then return categories
#FALLBACK
if the issue is unrelated to  , then the answer should be Choose one among of the categories of just say how can i assist you and mentioned all these categories 
This is a user complaint:
my girl friend left me 
"""

print(llm_ans(bad_prompt))