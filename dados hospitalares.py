import os
os.system("cls")

Vida_Plena = {
    1: ("Hemograma Completo", 2500.00),
    2: ("Raio-X", 2000.00),
    3: ("Ultrassonografia", 1800.00),
    4: ("Eletrocardiograma", 1000.00),
    5: ("Tomografia", 4000.00),
    6: ("Ressonância Magnética", 900.00),
    7: ("Exame de próstrata", 800.00)
}

exames = []
total = 0

print("\n-----------🏥 HOSPITAL VIDA PLENA 🏥-----------")
for codigo, (nome, preco) in Vida_Plena.items():
    print(f"{codigo} - {nome} | R${preco:.2f}")

while True:
    codigo = int(input("\nDigite o código do exame desejado (0 para encerrar): "))
    
    if codigo == 0:
        break

    if codigo in Vida_Plena:
        nome, preco_exame = Vida_Plena[codigo]
        exames.append((nome, preco_exame))
        total += preco_exame
        print(f"{nome} adicionado!")
    else:
        print("Código inválido!")

    continuar = input("Deseja agendar outro exame? (s/n): ").lower()
    if continuar != "s":
        break

formas = {
    1: ("Convênio", "Com desconto de 15%", 0.15),
    2: ("Particular", "Sem desconto", 0),
    3: ("Cartão de Crédito", "Com acréscimo de 8%", 0.08)
}

print("\n💸 Formas de Pagamento:")
for cod, (nome, desc_texto, taxa) in formas.items():
    print(f"{cod} - {nome} | ({desc_texto})")

while True:
    codigo_pag = int(input("\nDigite a opção da forma de pagamento (0 para sair): "))
    
    if codigo_pag == 0:
        print("Encerrando o programa...")
        exit()
    if codigo_pag in formas:
        nome_pag, desc_texto, taxa = formas[codigo_pag]
        
        
        if "desconto" in desc_texto.lower():
            total_final = total * (1 - taxa)
        elif "acréscimo" in desc_texto.lower():
            total_final = total * (1 + taxa)
        else:
            total_final = total

        print("----- RESUMO DO ATENDIMENTO -----")
        for nome_ex, preco_ex in exames:
            print(f"- {nome_ex}: R${preco_ex:.2f}")
            
        print("\n")
        print(f"Forma de pagamento: {nome_pag}")
        print(f"Total da conta: R${total_final:.2f} ({desc_texto})")
        print("\n")
        break 
    else:
        print("Opção de pagamento inválida! Tente novamente.")