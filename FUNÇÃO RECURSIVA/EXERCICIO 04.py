#4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros. 
def elementos(vetor):
    if len(vetor) == 0:
        return 0
    else:
        return vetor[0] + elementos(vetor[1:])
    
vetor=[1,10,86,14,12,24,6]
resultado = elementos(vetor)
print(resultado)
