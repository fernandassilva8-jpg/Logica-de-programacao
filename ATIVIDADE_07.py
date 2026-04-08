import os

os.system("cls")

def inflacionar(preco):
    if preco >= 100:
        resultado = preco * 1.20
    else:
        resultado = preco * 1.10
    return resultado
# SOLICITANDO DADOS 

preco_produto = float(input("Digite o preço do produto:"))
preco_produto = inflacionar(preco_produto)

print("- Solicitando dados -")
print(f"preço final: {preco_produto}")

