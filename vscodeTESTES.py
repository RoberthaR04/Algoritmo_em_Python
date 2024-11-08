#3) some as duas matrizes
a= [[-10, 1, 4, 6],
    [2, 3, 2,8]
    ]
b= [[1, 8, 4, -1],
    [0, 6, 3, -3]
    ]

result= [[0 for j in range(len(a[0]))] for i in range(len(a))] #cada loop tem uma funça, um vai percorrer as linhas e o outro vai percorrer as colunas
for i in range(len(a)): #len vai medir a matriz, esse loop vai percorrer cada linha
    for j in range(len(a[0])): #esse loop vai percorrer cada coluna
       result[i][j] = a[i][j] + b[i][j]
print(result)