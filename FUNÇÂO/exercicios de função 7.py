def fatorial(n):
    if n ==0:
        return 1
    elif n <0:
        return 'Não existe'
    else:
        fat = 1
        for i in range(n,1,-1):
            fat = fat*i
        return fat
x= int(input('Informe um número: '))
print('O fatorial:', fatorial(x))