import numpy as np

notas = np.array([9.9, 9.7, 9.8, 10, 10])

# Ordena as notas
notas_ordenadas = np.sort(notas)

# Remove uma instância da menor nota
notas_reduzidas = notas_ordenadas[notas_ordenadas != notas_ordenadas[0]]

# Remove uma instância da maior nota
notas_reduzidas2 = notas_reduzidas[notas_reduzidas != notas_reduzidas[-1]]

# Calcula a média das notas restantes
media_final = np.mean(notas_reduzidas2)

# Exibe o resultado
print(f"A média final do quesito é: {media_final:.2f}")

