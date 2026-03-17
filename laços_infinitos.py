import os 

os.system('cls')

while True: 
    idade = int(input('Digite uma idade: '))
    if idade < 18:
        print('Acesso negado!')
        print('Tente novamente...\n')
    else:
        print('Acesso permitido.')
        breack
print('Fim')