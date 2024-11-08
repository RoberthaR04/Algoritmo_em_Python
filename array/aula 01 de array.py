import numpy as np
a = np.array([])

for i in range(0,6):
    num = int(input('Digite um número: '))
    a = np.append(a,num)#comando adicionado sempre ao final
print(a)
