# aula1_questao1.py

# Solicita dois números decimais ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta e arredonda para duas casas decimais
diferenca = round(abs(num1 - num2), 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é: {diferenca}")
