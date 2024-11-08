import numpy as np
numeros = np.zeros(100, dtype=int)

for i in range(100):
    while True:
        matricula = int(input(f"Digite a matrícula {i+1}: "))
        # Verifica se a matrícula já existe no array
        if matricula in numeros:
            print("Matrícula já existente, tente novamente!")
        else:
            numeros[i] = matricula
    break  # Sai do loop while 


print("Matrículas cadastradas:")
for numero in numeros:
    print(numero)