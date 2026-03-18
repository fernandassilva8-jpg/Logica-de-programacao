import os 
os.system("cls")


login_correto = "Fernanda"
senha_correto = "TudoNosso123"

LOGIN_CORRETO = 3

while tentativas < 3:
    login = input("Digite seu login")
    senha = input("Digite sua senha: ")

    login_esta_correto = login == login_correto
    senha_esta_correta = senha == senha_correto

    if login_esta_correto and senha_esta_correta:
        print("Login bem-sucedido!")
        break #Interrompe o laço de repetição
    if chances_restantes > 0:
        print("Login ou senha incorretos. Tente novamente.")
        print(f"Você tem mais {chances_restantes} tentativas, boa sorte")
    else:
        print("acabou, acesso bloqueado!")
        break
