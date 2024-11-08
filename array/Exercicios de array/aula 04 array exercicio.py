import numpy as np
num=np.array([])

for i in range(3):
    numero=int(input('Informe um número:'))
    #append adiciona elemento no array
    num = np.append(num,numero)



y= int(input('Informe uma posição: '))
#solicitar uma posição válida entre 0 e
#len(num)-1
while y<0 or y>len(num)-1:
    y=int(input('Informe uma posição: '))





#a intenção é ir "chutando" até acertar a posição que o número estiver