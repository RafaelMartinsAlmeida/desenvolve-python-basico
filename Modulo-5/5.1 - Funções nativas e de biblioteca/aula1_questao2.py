# aula1_questao2.py

import random
import math

# Solicita ao usuário a quantidade de valores aleatórios
n = int(input("Quantos valores aleatórios você deseja gerar? "))

soma = 0

# Gera n números aleatórios de 0 a 100 e acumula a soma
for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

# Calcula a raiz quadrada da soma
raiz = math.sqrt(soma)

# Exibe o resultado
print(f"A raiz quadrada da soma dos valores é: {raiz:.2f}")
