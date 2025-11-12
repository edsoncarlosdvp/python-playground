from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])

prompt = input("Digite para interagir com a IA: ")

while prompt.lower() != "sair":
    response = chat.send_message(prompt)
    print(f"IA: {response.text}\n")
    prompt = input("Continue a sua interação com a IA (ou 'sair' para encerrar): ")