from pathlib import Path
from dotenv import load_dotenv
import os

import json
from interaction_ia import transform_data_for_json

# Carrega variáveis do .env
load_dotenv()

# Lê variável
assets_dir = os.getenv("ASSETS_DIR")

# Converte para Path
file_path = Path(assets_dir) / "resenhas_app_chatgpt.txt"

# Step 1
list_reviews = []

with open(f"../{file_path}", "r", encoding="utf-8") as file:
  for line in file:
    list_reviews.append(line.strip())

# Step 2 e  3
list_reviews_json = []

for review in list_reviews:
  review_json = transform_data_for_json(review)
  review_dictonary = json.loads(review_json)
  list_reviews_json.append(review_dictonary)

# Step 4
def count_join_item(list_reviews_dictnary):
  count_negative = 0
  count_neutral = 0
  count_positive = 0
  list_dictnary_str = []

  for review in list_reviews_dictnary:
    if review["avaliação"] == "Negativa":
      count_negative += 1
    elif review["avaliação"] == "Neutra":
      count_neutral += 1
    else:
      count_positive += 1
  
    list_dictnary_str.append(str(review))
  
  text_join = "####".join(list_dictnary_str)

  return count_negative, count_neutral, count_positive, text_join

positive, neutral, negative, texts = count_join_item(list_reviews_json)

print(f"Positivas: {positive}\n")
print(f"Neutras: {neutral}\n")
print(f"Negativas: {negative}\n")
print(texts)