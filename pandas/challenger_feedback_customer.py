import sys
import os
import time
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
  delay_time = 3 if review_number < len(collumns_reviews_text) - 1 else 0
  contents = model_ia_content(prompt, delay_time)
  result = f"Resenha {review_number + 1}: '{resenha}' -> Sentimento: {contents}"
  list_ranked_feedbacks.append(result)
  print(result)

  if review_number < len(collumns_reviews_text) - 1:
    time.sleep(3)
df_reviews["sentiment"] = list_ranked_feedbacks

df_negative_reviews = df_reviews[df_reviews["sentiment"] == "Negativo"]

df_unified_negative_reviews = "#####".join(df_negative_reviews)

prompt=f"""Você é um analista de dados. Vou te passar muitas resenhas negativas de
análises de um produto, separadas por "#####", e eu quero que você encontre 5 categorias diferentes
para os tipos de reclamações. Quero que você me retorne as 5 categorias.
Cada categoria deve ser uma frase curta, de no máximo 6 palavras.

Aqui estão as resenhas negativas: {df_unified_negative_reviews}"""

print("\n" + "="*60)
print("Analisando categorias de reclamações...")
print("="*60 + "\n")

contents = model_ia_content(prompt, 3)
result = f"Resultado: {contents}"
print(result)