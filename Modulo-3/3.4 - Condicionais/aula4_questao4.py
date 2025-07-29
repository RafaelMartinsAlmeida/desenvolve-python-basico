# aula4_questao4.py

# Solicita distância e peso
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Determina o valor por kg com base na distância
if distancia <= 100:
    preco_por_kg = 1.0
elif distancia <= 300:
    preco_por_kg = 1.5
else:
    preco_por_kg = 2.0

# Calcula o valor base do frete
valor_frete = preco_por_kg * peso

# Aplica taxa adicional se o peso for superior a 10 kg
if peso > 10:
    valor_frete += 10

# Exibe o valor do frete
print(f"Valor do frete: R${valor_frete:.2f}")
