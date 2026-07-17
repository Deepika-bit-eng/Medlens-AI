from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_medicine(name):

    prompt = f"""
You are a medical assistant.

Explain the medicine:

{name}

Return ONLY JSON.

{{
"name":"{name}",
"purpose":"",
"why_prescribed":"",
"common_side_effects":"",
"source":"",
"confidence":95
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text