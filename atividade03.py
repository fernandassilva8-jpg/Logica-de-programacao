import os

os.system('cls')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a == b:
    soma = a + b
    c = soma
    print(f'o resultado é:{c}')
elif a != b:
    multiplicacao = a * b
    c = multiplicacao 
    print(f'o resultado é: {c}')    