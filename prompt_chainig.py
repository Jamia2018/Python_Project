import os
from time import sleep
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Read API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kahan hai?")

# Create Groq client
client = Groq(api_key=my_api_key)

# Model name
model = "llama-3.3-70b-versatile"

# -------------------------
# Sample Job Description
# -------------------------

JD = """
We are hiring a Backend Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- REST APIs
- 2+ years experience
"""

# -------------------------
# Sample Resume
# -------------------------

RESUME = """
Name: Rashid Alam

Experience:
3 years as a Software Developer

Skills:
Python
FastAPI
MySQL
Docker
REST APIs
Git

Project:
Built a Food Delivery Backend using FastAPI and MySQL.

Deployed using Docker.
"""


# -------------------------
# Generic LLM Function
# -------------------------

def ask_llm(system_prompt, user_prompt):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content


# -------------------------
# Step 1 : Resume Skill Extraction
# -------------------------

def step1_res_extract():

    system_prompt = """
You are an expert HR assistant.

Extract only the technical skills from the candidate's resume.

Do not add explanations.
Do not invent skills.
Return only the skill list.
"""

    user_prompt = f"""
Extract skills from this resume:

{RESUME}
"""

    return ask_llm(system_prompt, user_prompt)


# -------------------------
# Step 2 : JD Skill Extraction
# -------------------------

def step2_JD_extract():

    system_prompt = """
You are an expert HR assistant.

Extract only the required technical skills from the Job Description.

Do not add explanations.
Return only the skill list.
"""

    user_prompt = f"""
Extract skills from this Job Description:

{JD}
"""

    return ask_llm(system_prompt, user_prompt)


# -------------------------
# Step 3 : Match Candidate
# -------------------------

def step3_match(candidate, jd):

    system_prompt = """
You are an expert HR assistant.

Compare the candidate's skills with the required job skills.

Return:

1. Match Score (1-100)
2. Matching Skills
3. Missing Skills
4. Short Verdict
"""

    user_prompt = f"""
Candidate Skills:

{candidate}

Job Description Skills:

{jd}
"""

    return ask_llm(system_prompt, user_prompt)


# -------------------------
# Main Program
# -------------------------

print("Extracting Resume Skills...")
candidate = step1_res_extract()

sleep(2)

print(candidate)

print("\nExtracting JD Skills...")
jd = step2_JD_extract()

sleep(2)

print(jd)

print("\nMatching Candidate...\n")

score = step3_match(candidate, jd)

print(score)            