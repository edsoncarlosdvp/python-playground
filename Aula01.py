# Aula01
print("Hello, World!")

# Aula02 - Variáveis, Operações Matemáticas e Concatenação de Strings
produto01 = 5
produto02 = 2000
produto03 = 1

nome_do_produto01 = "Macarrão"
nome_do_produto02 = "Celular"
nome_do_produto03 = "Bala"

print("O produto", nome_do_produto01, "tem o valor de R$", produto01)
print("O produto", nome_do_produto02, "tem o valor de R$", produto02)
print("O produto", nome_do_produto03, "tem o valor de R$", produto03)

# Aula03 - Operações Matemáticas e Variáveis em Python
amigos = 5
aluguel = 1000
supermercado = 500
carro = 400

total = aluguel + supermercado + carro

print("O total é de R$", total)

nome = "Pedro"
amigos = 6
aluguel = 1000
supermercado = 500
carro = 400

total_de_carros = carro * 2
total = aluguel + supermercado + total_de_carros

print("O total é de R$", total)

total_por_pessoa = total / amigos
print("O total por pessoa é de R$", total_por_pessoa)

# Nomeclatura e Tipos de Dados em Python: `int`, `float`, `str` e `bool`
decimal = carro / 3  # float
pedro_tem_carteira_de_motorista = True
type(aluguel) # int
type(decimal) # float
type(nome)    # str
type(pedro_tem_carteira_de_motorista) # bool

# Manipulando Strings em Python: Métodos `lower`, `upper`, `strip` e `replace`

texto = "   PeDRo da Silva SauRo  "

print(texto.lower())  # todas as letras minúsculas
print(texto.upper())  # todas as letras maiúsculas
print(texto.strip())  # remove espaços em branco no início e no fim
print(texto.replace("a", "@"))  # substitui 'a' por '@'

# Recebendo Dados do Usuário com `input` e Formatando Textos com fStrings
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"A pessoa se chama, {nome} e tem {idade} anos.")

# Estruturas Condicionais em Python: `if`, `elif` e `else`
name = "Carla Souza"
age = 32

if age < 18:
    print(f"{name} é menor de idade.")
elif age >= 18 and age < 65:
    print(f"{name} é adulta.")

avarage = 8.9
if avarage < 5:
    print("Reprovado")
elif avarage >= 5 and avarage < 7:
    print("Recuperação")
else:
    print("Aprovado")

# Conceitos de loops em Python: `while` e `for`

characters = 1
while characters <= 50:
    print("*", sep="-", end="")
    characters += 1

# Estrutura de Dados em Python: Listas e Dicionários

list_names = ["Ana", "Bruno", "Carlos", "Diana", "Edson"]
list_averages = [8.9, 7.5, 3.2, 9.5, 7.5]

# i = 0

# while i < len(list_averages):
#     list_averages[i] = min(list_averages[i] + 1, 10)
#     print(f"Nome: {list_names[i]} - Média: {list_averages[i]}")
#     i += 1

name = list_names[-2] # Acessa o penúltimo elemento da lista
print(name)

# Particionando uma lista
first_half = list_names[1:3] # Pega do índice 1 ao 2 (3 não incluso)

# Adicionando elementos no array
list_names.append("Fábio Carraro") # Adiciona no final da lista
list_names.append(["Márcio Gomes", "Ana Paula"]) # Adiciona uma lista como um único elemento
print(list_names[6][1]) # Acessa "Ana Paula"
list_names.insert(2, "Gabriela")    # Adiciona no índice 2
list_names.extend(["Hugo Souza", "Isabela Silveira"]) # Adiciona vários elementos no final da lista
list_names.remove(list_names[6][2]) # Remove "Isabela Silveira"

list_names = ["Ana", "Bruno", "Carlos", "Diana", "Edson"]
list_averages = [8.9, 7.5, 3.2, 9.5, 7.5]

ultimos_tres = list_names[-3:]  # Acessa os últimos três itens do dicionário
print(ultimos_tres)

# Estudando dicionários em Python

dictionary_students = {
    "Ana": 8.9,
    "Bruno": 7.5,
    "Carlos": 3.2,
    "Diana": 9.5,
    "Edson": 7.5
}

print(dictionary_students)

dictionary_challengers = [
    {
        "Nome": "Ana",
        "Média": 8.9,
    },
    {
        "Nome": "Bruno",
        "Média": 7.5,
    },
    {
        "Nome": "Carlos",
        "Média": 3.2,
    },
    {
        "Nome": "Diana",
        "Média": 9.5,
    },
    {
        "Nome": "Edson",
        "Média": 7.5,
    }
]

print(dictionary_challengers)

dictionary_product = [
    {"Nome": "Geladeira", "Preço": 3500, "Quantidade": 2},
    {"Nome": "IPhone 16", "Preço": 9900, "Quantidade": 1},
    {"Nome": "Switch II", "Preço": 4600, "Quantidade": 1},
]

for product in dictionary_product:
    preco = product["Preço"]

    if preco < 10000:
        preco *= 1.05

        preco = min(preco, 10000)
        product["Preço"] = preco

for p in dictionary_product:
    print(f"{p['Nome']} — Novo preço: R$ {p['Preço']:.2f}")