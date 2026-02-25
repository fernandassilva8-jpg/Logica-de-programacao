import os
# LIMPAR TERMINAL.
os.system("cls || clear")

idade = int(input("Digite sua idade"))

if idade >= 65:
    print("Não são obrigados a votar")
if idade >= 18:
    print ("Voto obrigatório")
if idade >= 16:
    print("voto opcional")
else:
    print("Não podem votar")

    
    
    

