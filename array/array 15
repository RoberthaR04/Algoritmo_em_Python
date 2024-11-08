import numpy as np

N= int(input("Qual será o número de elementos do vetor?"))

numeros= np.zeros(N, dtype=int) 

for i in range(N):
   numeros[i]= int(input(F"Digite o elemento {i+1}: "))
    
pares = numeros[numeros % 2 == 0]
impares = numeros[numeros % 2 != 0]

# Imprime os vetores de pares e ímpares
print("Valores pares:", pares)
print("Valores ímpares:",impares)