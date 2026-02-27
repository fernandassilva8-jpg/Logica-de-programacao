import os
os.system("cls || clear")

#Limpa o terminal
print(" -Solicitando dados -")
primeiro_inteiro = int(input("Digite o primeiro inteiro:"))
segundo_inteiro = int(input("Digite seu seu segundo inteiro:"))

 #Calculo
soma = primeiro_inteiro + segundo_inteiro
produto = primeiro_inteiro, segundo_inteiro
media = soma/2
maior = max(primeiro_inteiro, segundo_inteiro)
menor = min(primeiro_inteiro, segundo_inteiro)

#Condicional simples

print("\n- Exibindo resultados -")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"produto; {produto}")

if primeiro_inteiro == segundo_inteiro:
    print("Os números são iguais.")
else:
    print(f"Maior número: {maior}")
    print("Menor número: {Menor}")    