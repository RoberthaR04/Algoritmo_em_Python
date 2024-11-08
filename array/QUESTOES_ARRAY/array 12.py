import numpy as np

numeros=np.zeros(20, dtype=int)

for i in range(20):
    numeros[i]=int(input(f"Digite o número {i+1}: "))
    
for i in numeros:
    print(i) 
      
for i in range(10):  # Apenas até a metade do array
    numeros[i], numeros[19 - i] = numeros[19 - i], numeros[i]

# Imprime o vetor modificado
print("Vetor modificado:")
for i in numeros:
    print(i)
