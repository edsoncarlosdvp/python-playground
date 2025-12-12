import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from email_bodies import email_bodies
from model_ia.model_ia_content import model_ia_content


def email_summarizer():
    emails_formatted = "\n\n".join(f"E-mail {i+1}:\n{email}"
      for i, email in enumerate(email_bodies))
    
    print("Aguarde, preparando o resumo...\n")
    
    prompt = (
      "Resuma cada e-mail abaixo separadamente, mantendo a numeração. "
      "Use 1 a 2 frases por e-mail. "
      "Texto:\n\n"
      f"{emails_formatted}"
    )
    
    resumed = model_ia_content(prompt)
      
    return resumed

print(email_summarizer())