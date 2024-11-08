#mdc(máximo divisor comum)
def mdc(x,y):
    if y == 0:
        return x
    else:
        return mdc(y, x%y)

x = int(input('Informe um número: '))
y = int(input('Informe um número: '))
print(mdc(x,y))