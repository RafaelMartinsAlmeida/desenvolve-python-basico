# aula1_questao3.py

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

# Cálculo da média
m = (n1 + n2 + n3) / 3

# Verifico a situação do aluno com base na média
if m >= 60:
    print("Aprovado")
elif m > 40:
    print("Recuperação")
else:
    print("Reprovado")

# Independentemente do resultado, imprimo "Fim" no final
print("Fim")
