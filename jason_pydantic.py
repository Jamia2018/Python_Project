# ================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ================================

# os is used to read environment variables (like API keys)
import os

# Path helps work with file and folder paths.
# (Not used in this program, so you can remove it for now.)
from pathlib import Path

# load_dotenv() loads variables from the .env file
from dotenv import load_dotenv

# Groq is the client library used to communicate with the Groq AI API
from groq import Groq


# =====================================
# STEP 2: LOAD THE .env FILE INTO PYTHON
# =====================================

# Reads the .env file and makes its variables available
load_dotenv()


# ===================================
# STEP 3: READ THE API KEY FROM .env
# ===================================

# Look for a variable named GROQ_API_KEY
# Example:
# GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
my_api_key = os.getenv("GROQ_API_KEY")


# ===================================
# STEP 4: CHECK IF API KEY EXISTS
# ===================================

# If no API key was found, stop the program
if not my_api_key:
    raise ValueError("API key kaha hai bhai")


# ===================================
# STEP 5: CREATE A GROQ CLIENT
# ===================================

# Create an object that lets us communicate with Groq AI
client = Groq(api_key=my_api_key)


# ===================================
# STEP 6: CHOOSE THE AI MODEL
# ===================================

# This is the AI model we want to use
model = "llama-3.3-70b-versatile"

# The sender of the message is the user
role = "user"


# ===================================
# STEP 7: IMPORT PYDANTIC
# ===================================

# BaseModel helps us define a structured data model
from pydantic import BaseModel


# ===================================
# STEP 8: DEFINE THE OUTPUT STRUCTURE
# ===================================

# The AI should return these three fields only
class Ticket(BaseModel):

    # Customer's name
    name: str

    # Customer's email
    email: str

    # Customer's issue/problem
    issue: str


# ===================================
# STEP 9: CONVERT THE PYTHON CLASS
#         INTO A JSON SCHEMA
# ===================================

# AI understands JSON schema better than Python classes.
# This converts the Ticket class into JSON Schema.
schema = Ticket.model_json_schema()


# ===================================
# STEP 10: TELL THE AI TO RETURN JSON
# ===================================

# Instead of paragraphs,
# we want a proper JSON object.
response_format = {
    "type": "json_object"
}


# ===================================
# STEP 11: CREATE THE SYSTEM PROMPT
# ===================================

# This tells the AI:
# 1. Extract information.
# 2. Follow this schema.
# 3. Return only JSON.
system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.

{schema}
"""


# ===================================
# STEP 12: CREATE SYSTEM MESSAGE
# ===================================

# System messages tell the AI how it should behave.
message_system = {
    "role": "system",
    "content": system_prompt
}


# ===================================
# STEP 13: CUSTOMER TICKET
# ===================================

# This is the raw customer message.
# Notice that it contains extra information
# like address and phone number.
text = """
Hello My name is Md Rashid .

Yesterday I broke up with my girlfriend Sheetal.

I have an iPhone which is not working at all.

My address is Delhi.

My email is jmi.cse.@gmail.com.

i wanna say something about our education minister , have some shame just resigne plz 
My contact number is 82134.
"""


# ===================================
# STEP 14: CREATE THE USER PROMPT
# ===================================

# This is the instruction given to the AI.
prompt = f"""
This is a customer ticket.

Please extract the personal information from this.

{text}
"""


# ===================================
# STEP 15: CREATE USER MESSAGE
# ===================================

# The AI receives messages in dictionary format.
message = {
    "role": role,
    "content": prompt
}


# ===================================
# STEP 16: STORE ALL MESSAGES
# ===================================

# First comes the system message,
# then the user's message.
messages = [
    message_system,
    message
]


# ===================================
# STEP 17: SEND REQUEST TO GROQ
# ===================================

response = client.chat.completions.create(

    # Which AI model to use
    model=model,

    # Conversation messages
    messages=messages,

    # Force the AI to return JSON
    response_format=response_format
)


# ===================================
# STEP 18: GET THE AI RESPONSE
# ===================================

# The response object contains lots of information.
# We only want the actual answer.
answer = response.choices[0].message.content


# ===================================
# STEP 19: PRINT RAW JSON
# ===================================

print(answer)


# ===================================
# STEP 20: IMPORT JSON MODULE
# ===================================

# Used to convert JSON text into a Python dictionary.
import json


# ===================================
# STEP 21: CONVERT JSON STRING
#         TO PYTHON DICTIONARY
# ===================================

# answer is currently just text.
raw_json = answer

# Convert JSON text into a Python dictionary.
data_file = json.loads(raw_json)


# ===================================
# STEP 22: CREATE A PYDANTIC OBJECT
# ===================================

# **data_file unpacks the dictionary.
#
# Example:
#
# {
#   "name":"Pratyush",
#   "email":"abc@gmail.com",
#   "issue":"iPhone not working"
# }
#
# becomes
#
# Ticket(
#     name="Pratyush",
#     email="abc@gmail.com",
#     issue="iPhone not working"
# )
#
ticket = Ticket(**data_file)


# ===================================
# STEP 23: ACCESS THE DATA
# ===================================

# Print customer's name
print(ticket.name)

# Print customer's email
print(ticket.email)

# Print customer's issue
print(ticket.issue)