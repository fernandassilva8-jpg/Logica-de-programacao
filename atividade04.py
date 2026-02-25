import os
# Limpar terminal
os.system("cls || clear")

print(" - Solicitando dados -:")
quantidade = int(input("Digite a quantidade de maçãs"))

if quantidade < 12:
    preco = 1.30
else: 
    preco = 1
    
preco_final = quantidade * preco

print("\n- Exibindo resultado -")
print(f"Preço por maçã: R$ {preco:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

    

    


