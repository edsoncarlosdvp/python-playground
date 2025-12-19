import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from email_bodies import email_bodies
from model_ia.model_ia_content import model_ia_content


def email_summarizer():
    emails_formatted = "\n\n".join(f"E-mail {i+1}:\n{email}"
      for i, email in enumerate(email_bodies))
    prompt = (
      "Resuma cada e-mail abaixo separadamente, mantendo a numeração. "
      "Use 1 a 2 frases por e-mail. "
      "Texto:\n\n"
      f"{emails_formatted}"
    )
    
    print("Aguarde, preparando o resumo...\n")

    summarized = model_ia_content(prompt)

    with open("list_of_email_summaries.txt", "w", encoding="utf-8") as file:
      file.write(summarized + "\n")
      print("Resumo salvo em 'list_of_email_summaries.txt'.\n")

    response = input("Deseja ver o conteúdo do arquivo? (Digite Sim ou Não): ").strip().lower()

    if response in ("sim", "s"):
      with open("list_of_email_summaries.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(f"Conteúdo do arquivo:\n{content}\n")
        print("O conteúdo foi exibido com sucesso! Até mais!")

    else:
      print("Operação finalizada. Até mais!")

email_summarizer()