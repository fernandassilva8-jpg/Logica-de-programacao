import os

os.system (" cls || clear ")

# ENTRADA DE DADOS 
matricula = input (" Digite sua matrícula: ")

ano_nascimento = int(input("Digite seu ano de nascimento:"))

tempo_de_trabalho = int(input("Digite seu tempo de trabalho:"))

# PROCESSAMENTO 
idade = 2026 - ano_nascimento

if idade >= 65 or tempo_de_trabalho >= 30:
    resultado = "Requerer aponsentadoria"
else:
    resultado = "Não requerer aposentadoria"

# SAÍDA 
print ("\n - Resultado")
print (f"Idade {idade}:")
print (f"Tempo de trabalho {tempo_de_trabalho}:")
print (f"Resultado {resultado}:")


                        
