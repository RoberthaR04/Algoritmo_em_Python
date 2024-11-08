import numpy as np
A = np.array([])


def letras(N):
    a = []
    for i in range(N):
        numero = int(input("Informe um número inteiro: "))
        a.append(numero)
    return np.array(a)

N=int(input("informe a qtd de elemetos do vetor a: "))
A=letras(N)

M=int(input("informe a qtd de elemetos do vetor b: "))
B=letras(M)

i = 0
j = 0
C = []


    # Intercala os vetores A e B
while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

    # Adiciona os elementos restantes de A
while i < len(A):
    C.append(A[i])
    i += 1

    # Adiciona os elementos restantes de B
while j < len(B):
    C.append(B[j])
    j += 1

C = np.array(C)

print("Vetor intercalado:", C)