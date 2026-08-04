# # Import the 'os' module.
# # This module lets Python interact with your operating system.
# # We use it here to read environment variables (like API keys).
# import os

# # Import the load_dotenv() function from the python-dotenv package.
# # This function reads the .env file and loads its variables into Python.
# from dotenv import load_dotenv

# # Import the Groq class from the groq package.
# # This class is used to communicate with Groq's AI models.
# from groq import Groq


# # Load all variables from the .env file into the program.
# # Without this line, os.getenv() will not find values stored in .env.
# load_dotenv()


# # Read the value of the environment variable named "GROQ_API_KEY".
# #
# # Example:
# # .env file contains:
# # GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
# #
# # os.getenv("GROQ_API_KEY") returns:
# # gsk_xxxxxxxxxxxxxxxxx
# api_key = os.getenv("GROQ_API_KEY")


# # Print the API key to verify that it was loaded correctly.
# # Use this only while debugging.
# # Remove it before sharing your code or pushing to GitHub.
# print("API Key:", api_key)


# # Create a Groq client object.
# # This object is responsible for sending requests to Groq servers.
# #
# # We pass the API key using the keyword argument "api_key".
# client = Groq(api_key=api_key)


# # Send a request to Groq's AI model.
# response = client.chat.completions.create(

#     # Select which AI model to use.
#     model="llama-3.3-70b-versatile",

#     # Messages represent the conversation.
#     messages=[

#         # Every message is a dictionary.
#         {
#             # "user" means the message comes from the user.
#             "role": "user",

#             # This is the prompt that will be sent to the AI.
#             "content": "Hello"
#         },
#         {
#            "role": "user",
#            "content": "Can you brief explaine about amma khadija and why she popular known as amma khadija?" 
#         }
#     ]
# )


# # The response object contains lots of information.
# #
# # response
# # └── choices
# #     └── [0]
# #         └── message
# #             └── content
# #
# # We print only the AI's final answer.
# print(response.choices[0].message.content)


# # Print a message after everything finishes successfully.
# print("The End...")

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
role="user"
prompt="you are my strict office callegue who is also my manager"
# SYSTEM
message_system={
    "role": "system",
    "content": "I love you baby"
}
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]
# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, temperature=0)
# print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)