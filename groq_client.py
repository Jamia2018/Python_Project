# Import the os module.
# We use it to read environment variables like API keys.
import os

# Import load_dotenv() from the python-dotenv package.
# This function loads variables from the .env file into Python.
from dotenv import load_dotenv

# Import the Groq client.
# This is the library that lets us communicate with the Groq AI API.
from groq import Groq


# Load all variables from the .env file.
# Example:
# GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
load_dotenv()


# Read the value of GROQ_API_KEY from the .env file.
# os.getenv() returns the value if it exists.
# Otherwise, it returns None.
my_api_key = os.getenv("GROQ_API_KEY")


# Check whether the API key was found.
# "not my_api_key" means the key is missing or empty.
if not my_api_key:

    # Stop the program and show an error message.
    raise ValueError("API key kaha hai bhai")


# Create a Groq client object.
# This client will be used to send requests to the AI model.
client = Groq(api_key=my_api_key)


# Select the AI model we want to use.
model = "llama-3.3-70b-versatile"

# Define the role of the message.
# "user" means the message is coming from the user.
role = "user"


# Create Prompt 1
prompt1 = "Hi!"

# Create Prompt 2
prompt2 = "Explain time travel in detail but under 100 words"

# Create Prompt 3
prompt3 = "Write a 1000 word essay on Machine Learning"


# Store all prompts inside a list.
# This allows us to process them one by one using a loop.
prompts = [prompt1, prompt2, prompt3]


# Start a loop.
# Each time the loop runs, "prompt" becomes one item from the list.
for prompt in prompts:

    # Create one message in the format expected by the Groq API.
    # role = who is speaking
    # content = what they are saying
    message = {
        "role": role,
        "content": prompt
    }

    # The API expects a LIST of messages,
    # even if there is only one message.
    messages = [message]


    # Send the request to the AI model.
    response = client.chat.completions.create(

        # Which AI model to use.
        model=model,

        # The conversation/messages sent to the model.
        messages=messages,

        # Maximum number of tokens the AI is allowed to generate.
        max_tokens=5000
    )

# Print the AI's generated answer
print("AI Response:")
print(response.choices[0].message.content)


    # Print information about the request.
print(f"""
Prompt: {prompt}
-----------------------
Prompt Tokens     : {response.usage.prompt_tokens}
Completion Tokens : {response.usage.completion_tokens}
Total Tokens      : {response.usage.total_tokens}
Finish Reason     : {response.choices[0].finish_reason}
""")
    
    
#     Start Program
#       │
#       ▼
# Import libraries
#       │
#       ▼
# Load .env file
#       │
#       ▼
# Read GROQ_API_KEY
#       │
#       ▼
# API key exists?
#       │
#  ┌────┴────┐
#  │         │
# No        Yes
#  │         │
# Stop      ▼
#        Create Groq Client
#             │
#             ▼
#       Create 3 prompts
#             │
#             ▼
#       Store them in a list
#             │
#             ▼
#         Start for loop
#             │
#             ▼
#      Take one prompt
#             │
#             ▼
#       Create message
#             │
#             ▼
#      Send request to AI
#             │
#             ▼
#      Receive response
#             │
#             ▼
#      Print token usage
#             │
#             ▼
#   Next prompt (repeat)
#             │
#             ▼
#         Program ends