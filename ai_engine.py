import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found. Check your .env file.")

client = Groq(api_key=api_key)


def analyze_legal_document(document_text):

    prompt = f"""
You are an AI Legal Document Analysis Assistant.

Analyze the following legal document.

DOCUMENT:
{document_text}

Identify the following information:

1. Document Type
2. Parties Involved
3. Purpose of the Agreement
4. Duration
5. Key Obligations
6. Payment Terms
7. Termination Conditions
8. Confidentiality Clauses
9. Important Dates
10. Potentially Important Clauses

Also provide a simple summary of the document.

Instructions:
- Use only information present in the document.
- Do not invent facts.
- If information is missing, mention "Not specified".
- Use simple English.
- Organize the answer using headings and bullet points.
- Do not present the analysis as professional legal advice.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that analyzes legal documents."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
