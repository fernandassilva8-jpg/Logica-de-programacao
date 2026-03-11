import os

os.system

print("""
                           ATÉ 5 KG        |     ACIMA DE 5 KG 
    MORANGO         |  R$ 2.50 por KG      |    R$ 2.20 por KG
    MACA            |  R$ 1.80 por KG      |    R$ 1.50 por KG   
 """)

morango = int(input('Digite a quantidade de morango em KG: '))
maca = int(input('Digite a quantidade desejadas de maças em kilos: '))

if morango <= 5: 
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20
if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

total = preco_maca + preco_morango
peso_total = morango + maca
valor_compra = total

if maca or morango >= 10  or valor_compra > 15: 
    total = total * 0.90 
    print('Parabéns!!!!Você ganhou 10% de desconto!!!')