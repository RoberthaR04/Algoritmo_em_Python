import numpy as np 
numeros = np.zeros(10, dtype=float)#tipo float, pois são numeros reias

for i in range(10):
    numeros[i] = float(input(f'Informe o {i+1}º número real: '))
qtd_negativos = np.sum(numeros <0) #sum serve para verificar se existe valores negativos e informar a quantidade
qtd_positivo = np.sum(numeros[numeros >0]) #vai filtrar somente os positivos e calcular eles

print(f"A quantidade de números negativos é: {qtd_negativos} ") #informa para o usuaário 
print(f"A soma dos números positivos é: {qtd_positivo:.2f} ")

