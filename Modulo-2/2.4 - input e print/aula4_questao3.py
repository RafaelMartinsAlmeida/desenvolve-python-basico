# aula4_questao3.py

# Leitura dos dados do produto 1
produto1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

# Leitura dos dados do produto 2
produto2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

# Leitura dos dados do produto 3
produto3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Cálculo do preço total
total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)

# Exibindo o resultado formatado
print(f"Total: R${total:,.2f}")
