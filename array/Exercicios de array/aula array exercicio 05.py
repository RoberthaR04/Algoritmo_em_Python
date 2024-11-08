import numpy as np
num=np.array([])
num(num, numero)
cont=0
for i in range(5):
    if num[i] %2==0:
        cont=cont + 1

pos= np.where(num%2==0)
print(pos)
pares = num[pos]
print(pares)

