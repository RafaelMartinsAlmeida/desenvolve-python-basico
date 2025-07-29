# aula4_questao1.py

# Leitura das dimensões do terreno e do preço do metro quadrado
comprimento = int(input("Digite o comprimento do terreno (em metros): "))
largura = int(input("Digite a largura do terreno (em metros): "))
preco_m2 = float(input("Digite o preço do metro quadrado: "))

# Cálculo da área do terreno
area_m2 = comprimento * largura

# Cálculo do valor total do terreno
preco_total = preco_m2 * area_m2

# Exibindo o resultado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
