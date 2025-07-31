# aula1_questao5.py

import emoji

# Mostra os emojis disponíveis
print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:\n")

# Pede uma frase codificada
frase = input("Digite uma frase e ela será emojizada:\n")

# Converte os códigos de emoji para os emojis visuais
frase_emojizada = emoji.emojize(frase, language="alias")

# Exibe a frase com emojis
print("\nFrase emojizada:")
print(frase_emojizada)