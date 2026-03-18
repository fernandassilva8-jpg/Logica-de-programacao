import os 

os.system("cls")

# if idade < 18:
#     print("Bem-vindo, pode entrar")
#     print("Deseja alguma bebida?")
# else:
#     print("Desculpe, você não pode entrar")

login_correto = "Marta"
senha_correto = "123abc"

while True:
    login = input("Digite seu login")
    senha = input("Digite sua senha: ")

    login_esta_correto = login == login_correto
    senha_esta_correta = senha == senha_correta

    if login_esta_correto and senha_esta_correta:
        print("Login bem-sucedido!")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")


