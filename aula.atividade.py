import os
#LIMPAR TERMINAL.
os.system ("cls || clear")

print  ( " -  Solicitando dados -")
primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo numero:"))
 
 
soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)
 
print(" \n- Exibindo resultados - ")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
 
 
# Verificando o maior valor e o menor.
 
if primeiro_numero == segundo_numero:
    print("Os numeros são iguais")
else:
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        
        
              
        
    
    
    