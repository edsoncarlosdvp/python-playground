import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

def model_ia_content(prompt: str, delay: int = 0):
  model = genai.GenerativeModel("gemini-2.5-flash")
  response = model.generate_content(prompt)
  
  if delay > 0:
      time.sleep(delay)

  return response.text