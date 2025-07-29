# aula1_questao4.py

n = int(input("Digite a quantidade de números: "))
maior = 0

# Enquanto ainda restarem números a serem digitados
while n > 0:
    x = int(input("Digite um número: "))
    
    # Verifico se o número atual é maior que o anterior armazenado
    if x > maior:
        maior = x

    # Reduzo o contador
    n -= 1

# Ao final, mostro qual foi o maior número digitado
print("Maior:", maior)
