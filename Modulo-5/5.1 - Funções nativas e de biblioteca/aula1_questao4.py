# aula1_questao4.py

from datetime import datetime

# Pega a data e hora atuais
agora = datetime.now()

# Formata os valores para sempre terem dois dígitos
data_formatada = f"{agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"{agora.hour:02d}:{agora.minute:02d}"

# Exibe a data e a hora
print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
