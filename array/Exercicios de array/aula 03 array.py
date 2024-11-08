import numpy as np 
num = np.array([])

for i in range(6):
    numero=int(input('Informe um número: '))
    num= np.append(num,numero)#append adiciona elementos ao array
print(numero)
print(num)
#elevando ao quadrado
numq=num**2
print(numq)