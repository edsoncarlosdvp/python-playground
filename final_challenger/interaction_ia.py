from openai import OpenAI

client_openai = OpenAI(
  base_url="http://127.0.0.1:1234/v1",
  api_key="lm-studio-api-key-example",
)

def transform_data_for_json(data):
  response_llm = client_openai.chat.completions.create(
    model="google/gemma-3n-e4b",
    messages=[
      {
        "role": "system",
        "content": "Você é um especialista em análise de dados e conversão de dados para JSON."
      },
      {
        "role": "user",
        "content": f"""Você receberá uma linha de texto que representa uma resenha de um aplicativo em um marketing place online.
        Eu quero que você analise essa resenha e me retorne um JSON com as seguintes chaves:
        - 'usuário': o nome do usuário que fez a resenha
        - 'resenha_original': a resenha no idioma original que você recebeu
        - 'resenha_traduzida': a resenha traduzida para o português do Brasil
        - 'avaliação': a nota que o usuário deu para o aplicativo, 'Negativa', 'Neutra' ou 'Positiva' (apenas uma dessas opções)
        
        Exemplo de entrada:
        '879485937$Pedro Silva$This a positive review for the app'
        
        Exemplo de saída:
        {{
          "usuário": "Pedro Silva",
          "resenha_original": "This a positive review for the app",
          "resenha_traduzida": "Esta é uma resenha positiva para o aplicativo",
          "avaliação": "Positiva"
        }}
        
        Resenha a analisar: {data}"""
      }
    ],
    temperature=1.0,
  )

  response = response_llm.choices[0].message.content.replace("```json", "").replace("```", "")

  print(response)
  return response