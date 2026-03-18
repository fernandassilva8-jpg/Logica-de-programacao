# import os
# os.system("cls")

# senha = "fernandabonita"
# tentativa_senha = input("Digite sua senha: ")
# if senha != tentativa_senha:
#     print("acesso negado")
# else:
#     print("isso ai, acesso liberado")

import os 

os.system("cls")

nota = float(input("Digite sua nota: "))
if nota >= 7:
    print("Parabéns, você está aprovado")
elif nota >= 5:
    print("Você está em recuperação!")
else:
    print("você está reprovado")
