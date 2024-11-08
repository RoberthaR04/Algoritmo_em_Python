
def regressiva(i):
    print (i)
    if i <= 1: #caso base(não chama a si mesma)
        return 
    else: #caso recursivo(chama a si mesma)
        regressiva(i-1)
i=int(input("Informe número:"))