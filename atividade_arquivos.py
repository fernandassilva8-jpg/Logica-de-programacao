import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self):
        print(f'autor: {self.autor}')
        print(f'categoria: {self.categoria}\n')
        print(f'preço {self.preco}\n')
    def mostrar_linha(self):
        print("-"*33)
QUANTIDADE_LIVROS = 3
lista_livros = []

print('= Solicitnado dados =')
for i in range(QUANTIDADE_LIVROS):
    novo_livros = Livro(
        nome=input('Olá, por gentileza digite o nome do livro: '),
        autor=input('Digite também o nome do autor: '),
        categoria=input('Agora digite também qual a categoria do livro: '),
        preco=input('E por fim, qual o preço do livro?'),
    )
    print('')
    lista_livros.append(novo_livros)

print('= Salvando dados =')
with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
    for livros in lista_livros:
        arquivo.write(f'{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preco}\n')
    print('Salvo com sucesso!')
print( '= Consultando arquivo =')

with open('catalogo_livros.csv', 'r') as arquivo:
    for linha in arquivo:
        nome, autor, categoria, preco = linha.strip().split(',')
        lista_livros.append(Livro(
            nome=nome,
            autor=autor,
            categoria=categoria,
            preco=preco
        ))
for livro in lista_livros:
    livro.mostrar_dados()

print('= Fim do programa. =')

