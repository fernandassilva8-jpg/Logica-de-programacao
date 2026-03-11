import os
import time
os.system('cls')

#Limpar terminal


# for i in range(1,11,1): 
#     print(i)
#     # Espera dois segundos.
#     time.sleep(1) #Espera dois segundos.

# De 10 até 1

numero = int(input('Digite um numero: '))
for numero in range(numero, -1, -1): 
    print(numero)
    time.sleep(1)  #Espera um segundo.
