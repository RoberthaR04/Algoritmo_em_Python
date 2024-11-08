
#2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
def recursiva(fibon):
    if fibon == 1:
        return 0
    elif fibon == 2:
        return 1
    else:
        return recursiva(fibon- 1) + recursiva(fibon-2)
fibon= 10
print(recursiva(fibon))