import os

os.system('cls')

nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: ')
estado_civil = input('Digite seu estado civil: ')

if sexo == 'feminino' and estado_civil == 'casada':
   tempo = int(input('Digite o tempo de casamento: '))
   print(f'Tempo de casamento: {tempo} anos')
   
print(f'Nome: {nome} \n Sexo: {sexo} \n Estado Civil: {estado_civil}')
