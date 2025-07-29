# aula2_questao3.py
idade = int(input("Digite sua idade: "))
jogou_3_vezes = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ").lower() == 'true'
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica as condições de admissão no clube
pode_entrar = 16 <= idade <= 18 and jogou_3_vezes and vitorias > 0
print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_entrar}")
