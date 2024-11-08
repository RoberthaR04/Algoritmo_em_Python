import numpy as np
a = np.array([])

for i in range(0,6):
    num = int(input('Digite um número: '))
    a = np.append(a,num)#comando adicionado sempre ao final

soma = a[0] +a[1] +a[5]
print(soma)
print('Inicial',a)
a[4]=100
print('alterado',a)#letra C da atividade

for i in range(0,6):#letra D da atividade
    print(a[i])
