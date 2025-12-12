from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

def model_ia_content(prompt: str):
  model = genai.GenerativeModel("gemini-2.5-flash")
  response = model.generate_content(prompt)

  return response.text