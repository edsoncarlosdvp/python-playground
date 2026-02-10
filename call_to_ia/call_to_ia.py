from openai import OpenAI

client_openai = OpenAI(
  base_url="http://127.0.0.1:1234/v1",
  api_key="lm-studio-api-key-example",
)

response_llm = client_openai.responses.create(
  model="google/gemma-3n-e4b",
  input="Qual é a capital da França?",
  temperature=1.0,
)

print(response_llm.output_text)