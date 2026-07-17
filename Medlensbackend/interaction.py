from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def check_interactions(medicine_names):

    prompt = f"""
You are a medical safety assistant.

Check interactions between these medicines:

{", ".join(medicine_names)}

Return ONLY JSON.

{{
    "risk":"Low/Medium/High",
    "summary":"",
    "interactions":[
        {{
            "medicine1":"",
            "medicine2":"",
            "severity":"",
            "reason":""
        }}
    ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    text = response.text.replace("```json","").replace("```","").strip()

    return json.loads(text)