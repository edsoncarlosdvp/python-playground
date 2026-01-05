import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from model_ia.model_ia_content import model_ia_content

df_reviews = pd.read_csv('assets/reviews.csv')

collumns_reviews_text = df_reviews["reviewText"]

list_ranked_feedbacks = []
for review_number, resenha in enumerate(collumns_reviews_text):
  prompt = f"""Você irá analisar a resenha que eu te mandarei abaixo, e retornar com uma análise de sentimento
              Você deve responder apenas com uma das seguintes palavras: "Positivo", "Negativo" ou "Neutro",
              indicando o sentimento relativo aquela resenha especifica. Exemplos:
              'Eu adorei esse produto' -> Positivo
              'Gostei, mas não é nada especial' -> Neutro
              'Odiei esse produto' -> Negativo
              
              Segue a resenha para ser analisada: {resenha}"""
  contents = model_ia_content(prompt)
  result = f"Resenha {review_number + 1}: '{resenha}' -> Sentimento: {contents}"
  list_ranked_feedbacks.append(result)
  print(result)