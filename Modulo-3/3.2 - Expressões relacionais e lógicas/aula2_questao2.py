# aula2_questao2.py
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se pelo menos uma é maior de 17
pode_entrar = idade_juliana > 17 or idade_cris > 17
print(pode_entrar)
