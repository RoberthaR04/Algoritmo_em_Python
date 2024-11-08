#1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N. 
def fat(numero):
    if numero == 0:
        return 1
    else:
        return numero*fat(numero-1)
numero=int(input('Informe um numero inteiro: '))
print(fat(numero))











