# aula4_questao2.py

# Solicita a avaliação do usuário
avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))

# Verifica e imprime a mensagem correspondente
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um número de 1 a 5.")
