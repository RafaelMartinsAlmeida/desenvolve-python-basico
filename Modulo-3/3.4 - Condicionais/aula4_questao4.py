# aula4_questao4.py
distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

# Calculo do frete
if distancia <= 100:
    frete = peso * 1
elif 101 <= distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2

# Taxa adicional para pacotes acima de 10kg
if peso > 10:
    frete += 10

print(f"O valor do frete é R${frete:.2f}")
