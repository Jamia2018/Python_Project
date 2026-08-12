import os
from dotenv import load_dotenv
from groq import Groq


# --------------------------------------------------
# 1. Load .env file
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# 2. Get API key
# --------------------------------------------------

my_api_key = os.getenv("GROQ_API_KEY")


if not my_api_key:
    raise ValueError("Where is the API key?")


# --------------------------------------------------
# 3. Create Groq client
# --------------------------------------------------

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"


# --------------------------------------------------
# STEP 1: KNOWLEDGE BASE
# --------------------------------------------------

knowledge_base = {
    "age": "Rashid is 24 years old.",
    "software_developer": "Rashid is a Java Full Stack Developer with AI skills."
}


# --------------------------------------------------
# STEP 2: RETRIEVAL
# --------------------------------------------------

def retrieve_info(question):

    question = question.lower()

    if "age" in question:
        return knowledge_base["age"]

    elif "software developer" in question:
        return knowledge_base["software_developer"]

    else:
        return None


# --------------------------------------------------
# STEP 3: ASK LLM
# --------------------------------------------------

def ask_llm(question):

    # Retrieve information from our knowledge base
    context = retrieve_info(question)

    # If nothing was found
    if context is None:
        context = "No relevant information was found."


    # System instruction
    system_prompt = f"""
Answer in one line only.

Answer ONLY based on the context below.
Do not use outside knowledge.
Do not hallucinate.

Context:
{context}
"""


    # Messages sent to the LLM
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]


    # Send request to Groq
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )


    # Get AI answer
    answer = response.choices[0].message.content


    return answer


# --------------------------------------------------
# STEP 4: TEST
# --------------------------------------------------
question1 = "What is RAG in AI?"
answer1 = ask_llm(question1)
print(answer1)

question2 = "What is Rashid's age?"
answer2 = ask_llm(question2)
print(answer2)
