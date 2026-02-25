import os
# LIMPA O TERMINAL.
os.system(" cls || clear")

print("- Solicitando dados -")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero =  int(input("Digite o segundo número: "))

maior = max(primeiro_numero, segundo_numero)
menor = min(segundo_numero, segundo_numero)

print("\n- Exibindo resultado -")
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número:{segundo_numero}")
print(f"Maior número: {maior}")
print(f"Menor número {menor}")
