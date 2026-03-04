import os

# Limpar o terminal.
os.system ("cls")

usuario = int(input("Digite a sua média: "))
usuario2 = int(input("Digite o número de faltas:" ))
print("- Solicitando dados -")

#Condicional

if usuario < 7 and usuario2 >= 41:
    resultado = "reprovado"
else:
    resultado = "aprovado"

# Mostre a média e o número de faltas
print('\n-   Exibindo dados - ')
print(f"Média: {usuario} do aluno.")
print(f"Faltas: {usuario2} do aluno.")
print(f'Resultado: {resultado}.')