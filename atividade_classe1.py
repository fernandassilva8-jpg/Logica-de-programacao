import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cnpj: {self.cnpj}')
        print(f'Telefone: {self.telefone}')


lista_empresas = []

print('- Solicitando os dados -')
while True:
    empresa = Empresa(
        nome= input('Digite o nome da empresa: '),
        cnpj= input('Digite o cnpj da empresa: '),
        telefone= input('Digite o telefone da empresa: ')
    )
    lista_empresas.append(empresa)

    for empresa in lista_empresas:
        empresa.mostrar_dados()

    with open('lista_empresas.csv', 'a', encoding='utf-8') as arquivo:
        for empresa in lista_empresas:
            arquivo.write(f'{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n')
        print('Salvo!')

    nova_empresa = input('Deseja adicionar uma nova empresa? (s/n): ')
    if nova_empresa == 'n':
        print('Programa encerrado.')
        break