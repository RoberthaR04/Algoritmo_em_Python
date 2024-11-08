#0)lista = ['A', 1, 2, 'CASA', 2.3]
#print(lista)

#0) lista1 = [1, 4, 7, 8]
# lista2 = lista1.copy()
# print(lista2)
# lista1[2]=90
# print(lista2)

#1)Faça um programa para ler e imprimir uma matriz 2 x 4 de numeros inteiros.
lista = []
for i in range(2):
    linha = []
    for j in range(4):
        linha.append(int(input('Informe um valor: ')))
    lista.append(linha)
print(lista)
