import os

os.system("cls")

primeiro_numero = int(input("Digite o primeiro número: "))
operador = str ("Digite a operação desejada (+ - * /): ")
segundo_numero = int(input("Digite o segundo número: "))

match operador:
    case "+":
        resultado= primeiro_numero + segundo_numero
    case "-":
        resultado= primeiro_numero - segundo_numero
    case "*":
        resultado= primeiro_numero * segundo_numero
    case "/":
        resultado= primeiro_numero / segundo_numero
    case _:
        print("Opção inválida.")
        resultado = 0
        print(f"Resultado: {resultado}")