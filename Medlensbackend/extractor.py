from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_prescription(image_path):
    with open(image_path, "rb") as f:
        image = f.read()

    prompt = """
You are an expert medical prescription reader.

Carefully analyze the prescription image.

Extract ALL medicines even if the handwriting is difficult.

If you are uncertain, make your best guess and mark it with "confidence":"Low".

Return ONLY JSON.
Do NOT use markdown.
Do NOT wrap the response inside ```json.
Do NOT add explanations.

Output must begin with {
and end with }.

{
  "patient_name":"",
  "doctor_name":"",
  "medicines":[
    {
      "name":"",
      "dosage":"",
      "frequency":"",
      "duration":"",
      "confidence":"High"
    }
  ]
}

Never leave medicines empty unless absolutely impossible.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            prompt,
            types.Part.from_bytes(
                data=image,
                mime_type="image/jpeg"
            )
        ]
    )

    return response.text