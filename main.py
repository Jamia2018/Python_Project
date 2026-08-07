import json
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq
from pydantic import BaseModel
from pypdf import PdfReader

load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
model = "openai/gpt-oss-120b"


# ------------------ Pydantic Models ------------------

class Experience(BaseModel):
    company: str | None = None
    role: str | None = None
    duration: str | None = None
    description: str | None = None
    skills_used: list[str] = []


class Resume(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    total_experience_years: float | None = None
    skills: list[str] = []
    experiences: list[Experience] = []
    education: list[str] = []
    projects: list[str] = []
    certifications: list[str] = []


class ChatRequest(BaseModel):
    question: str


resume_schema = Resume.model_json_schema()


# ------------------ PDF Reader ------------------

def read_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ------------------ Resume Parser ------------------

def parse_resume(resume_text):
    system_prompt = f"""
You are an expert resume parser.

Return ONLY valid JSON matching this schema.

Schema:
{resume_schema}
"""

    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": resume_text,
            },
        ],
    )

    data = json.loads(response.choices[0].message.content)

    return Resume(**data)


# ------------------ Chat ------------------

def ask_candidate(question, resume):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": f"""
You are an AI recruiter.

Use ONLY this resume.

{resume.model_dump_json(indent=2)}
""",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.choices[0].message.content


# ------------------ Routes ------------------

@app.get("/")
def home():
    return {
        "message": "This is a home page!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    pdf_path = Path("my_resume.pdf")

    if not pdf_path.exists():
        return {
            "error": "my_resume.pdf not found."
        }

    resume_text = read_pdf(pdf_path)

    resume = parse_resume(resume_text)

    answer = ask_candidate(request.question, resume)

    return {
        "answer": answer
    }