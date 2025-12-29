import pandas as pd
import numpy as np

# Configuração para garantir que os números sejam os mesmos sempre que rodar (opcional)
np.random.seed(42)

# Listas de base para gerar os dados
nomes_base = ['Smartphone', 'Notebook', 'Fone de Ouvido', 'Monitor', 'Teclado', 'Mouse', 
              'Camisa', 'Calça', 'Tênis', 'Mochila', 'Cadeira Gamer', 'Mesa', 
              'Lâmpada Smart', 'Cafeteira', 'Liquidificador', 'Relógio', 'Tablet']

categorias_base = ['Eletrônicos', 'Vestuário', 'Móveis', 'Eletrodomésticos', 'Acessórios', 'Brinquedos']

# Gerando 50 linhas de dados
dados = {
    'Nome do produto': [f"Produto N. {i}" for i in range(1, 51)],
    'Categoria do produto': [np.random.choice(categorias_base) for _ in range(50)],
    'Preço do produto': np.round(np.random.uniform(50.0, 5000.0, 50), 2),
    'Itens vendidos': np.random.randint(1, 100, 50),
    'Avaliação do produto': np.round(np.random.uniform(1.0, 5.0, 50), 1)
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo as primeiras linhas
#print(df["Categoria do produto"]) # Exibe a coluna "Categoria do produto"
#print(df["Categoria do produto"].unique()) # Exibe os valores únicos da coluna "Categoria do produto"
#set(df["Categoria do produto"]) # Outra forma de exibir os valores únicos
#print(df)
#print(df[df["Categoria do produto"] == "Eletrônicos"]) # Filtra e exibe apenas os produtos da categoria "Eletrônicos"
#df_produtos_baixa_avaliacao = df[df["Avaliação do produto"] < 2.0] # Filtra e exibe apenas os produtos com avaliação menor que 2.0
#print(df_produtos_baixa_avaliacao.shape) # Exibe a quantidade de linhas e colunas do DataFrame filtrado

#df_produtos_eletronicos_preco_baixo = df[(df["Categoria do produto"] == "Eletrônicos") & (df["Preço do produto"] < 400.0)] # Filtra e exibe apenas os produtos da categoria "Eletrônicos" com preço menor que 1000.0
#print(df_produtos_eletronicos_preco_baixo) # Exibe o DataFrame filtrado
#print(df.iloc[15:21]) # Exibe as linhas de índice 15 a 20 (21 não incluso)

# Criando o novo DataFrame a partir do anterior
# O parâmetro 'inplace=False' garante que criamos um novo objeto sem alterar o original
df_products_with_index = df.set_index('Nome do produto')

# Exibindo as primeiras linhas
products_toys = df_products_with_index[df_products_with_index["Categoria do produto"] == "Brinquedos"]
#print(df_products_with_index.loc[['Produto N. 5', 'Produto N. 10', 'Produto N. 20'], ['Preço do produto', 'Itens vendidos']]) # Exibe as linhas do índice 'Notebook Mod. 2' até 'Monitor Mod. 5'
df_new_category = df_products_with_index.loc[products_toys.index, "Categoria do produto"] = "Infanto-juvenil" # Altera a categoria dos produtos de brinquedos para "Infanto-juvenil"
print(df_new_category)