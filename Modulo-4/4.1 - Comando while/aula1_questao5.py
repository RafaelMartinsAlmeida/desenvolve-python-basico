# aula1_questao5.py

# Leia a quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Verifico se há pelo menos um respondente
if N <= 0:
    print("Nenhum respondente informado.")
else:
    soma_idades = 0

    for i in range(N):
        idade = int(input(f"Digite a idade do respondente {i+1}: "))
        soma_idades += idade

    media = soma_idades / N
    print(f"A média das idades é: {media:.2f}")
