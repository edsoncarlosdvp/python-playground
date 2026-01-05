import sys
import os
from time import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from model_ia.model_ia_content import model_ia_content
import pandas as pd

def question_and_answer():
  list_of_questions = [
    "Quem é o Sonic?",
    "Quando foi lançado o primeiro jogo do Sonic?",
    "Quais são os principais inimigos do Sonic?",
    "Quais são as habilidades especiais do Sonic?",
    "Quais os jogos mais vendidos da SEGA?",
    "Quais jogos da SEGA foram adaptados para filmes?",
    "Qual é o console mais vendido da SEGA?",
    "Qual é o console mais vendido da Nintendo?",
    "Qual é o console mais vendido da Sony?",
    "é o console mais vendido da Microsoft?"
  ]

  os.makedirs("pandas", exist_ok=True)
  with open("pandas/questions_and_answer.txt", "w", encoding="utf-8") as file:
    for question in list_of_questions:
      file.write(question + "\n")

  dict_read_questions = []
  with open("pandas/questions_and_answer.txt", "r", encoding="utf-8") as file:
    for line in file:
      dict_read_questions.append(line.strip())

  for question in dict_read_questions:
    prompt = (
      "Responda de forma clara e objetiva as perguntas." 
      "Seja sucinto e direto ao ponto. " 
      "Use no máximo 15 palavras por resposta."
      "Perguntas:\n\n" f"{question}"
    )
    print("Aguarde, as respostas estão sendo formuladas...\n")
    answer = model_ia_content(prompt)
    dict_read_questions.append({"pergunta": question, "resposta": answer})

  with open("pandas/questions_and_answer.csv", "w", encoding="utf-8") as file:
    file.write("pergunta,resposta\n")
    
    for dict_question in dict_read_questions:
      file.write(f"{dict_question['pergunta']}, {dict_question['resposta']}\n")

  df = pd.DataFrame(dict_read_questions)
  df.to_csv("pandas/questions_and_answer.csv", index=False, encoding="utf-8")
  print("Arquivo CSV criado com sucesso!")
  print(df)
question_and_answer()