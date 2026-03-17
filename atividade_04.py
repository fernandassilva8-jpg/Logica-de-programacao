import os

os.system ('cls')
soma = 0

for i in range(3):
    nota = float(input('Digite uma nota: '))
    soma = soma + nota
    media = soma / 3  

print(f'Média: {media}')

if media >= 7:
    print('Aluno aprovado')
elif media < 7:
    print('Aluno em recuperação')
elif media < 4:
    print('Aluno reprovado')


