# aula1_questao3.py

import random

# Gera número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    elif palpite > numero_aleatorio:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero_aleatorio}.")
        break
