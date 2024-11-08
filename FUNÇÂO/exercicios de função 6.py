def par(numero):
    if numero%2 ==0:
        return 1
    else:
        return 0
x= int(input('Informe um número: '))
if par(x) ==1:
    print('Par')
else:
    print('Ímpar')