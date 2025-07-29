# aula1_questao6.py

# Leia a quantidade de experimentos registrados
N = int(input("Digite o número de experimentos registrados: "))

# Inicializo os contadores
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Loop para entrada dos dados dos experimentos
for i in range(N):
    entrada = input(f"Experimento {i+1} (ex: 10 C): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1]

    total_cobaias += quantia

    # Atualizo o contador correto de acordo com o tipo de cobaia
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

# Calculo os percentuais com verificação para evitar divisão por zero
if total_cobaias > 0:
    percentual_sapos = (total_sapos / total_cobaias) * 100
    percentual_ratos = (total_ratos / total_cobaias) * 100
    percentual_coelhos = (total_coelhos / total_cobaias) * 100
else:
    percentual_sapos = percentual_ratos = percentual_coelhos = 0

# Mostro os resultados finais
print("\nRELATÓRIO FINAL:")
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
