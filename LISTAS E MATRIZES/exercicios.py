#a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(a)
#1)Faça um programa para ler e imprimir uma matriz 2 x 4 de numeros inteiros.
lista = []
for i in range(2):
    linha = []
    for j in range(4):
        linha.append(int(input('Informe um valor: ')))
    lista.append(linha)
print(lista)

# #2.1)soma dos elementos da primeira coluna
matriz=[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
col=0 #define a coluna que vai ser somada
soma= sum(linha[col] for linha in matriz) #sum soma todos os valores - o "for" percorre caada linha
print(soma)

#2.2)produto da primeira linha
produto= 1
linha= matriz[0] #zero é a posição inicial da matriz
for elemento in linha: #percorre a linha
    produto *= elemento
print(produto)

#2.3)soma de todos os elementos
somat= 0
for linha in matriz:#para percorrer cada linha
    for elemento in linha: #vai percorrer os elementos de caada linha
        somat +=elemento

print(somat)


#2.4) o produto da diagonal principal
produto_di= 1
for i in range(len(matriz)):
    produto_di *= matriz[i][i] #[i] representa o indice da linha e da coluna
print(produto_di)


#3) some as duas matrizes
a= [[-10, 1, 4, 6],
     [2, 3, 2,8]]
b= [[1, 8, 4, -1],
     [0, 6, 3, -3]]

result= [[0 for j in range(len(a[0]))] for i in range(len(a))] #cada loop tem uma funça, um vai percorrer as linhas e o outro vai percorrer as colunas
for i in range(len(a)): #len vai medir a matriz, esse loop vai percorrer cada linha
    for j in range(len(a[0])): #esse loop vai percorrer cada coluna
        result[i][j] = a[i][j] + b[i][j]
print(result)


# #4) gere a matriz oposta
matriz=[[2, -3],
     [-1, 4]]

oposto= [[0 for j in range(len(matriz[0]))] for i in range(len(matriz))]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        oposto [i][j]= -matriz[i][j]
print('Matriz oposta: ',oposto)
print('Matriz original: ' ,matriz)

# Verificando se A + (-A) resulta em zeros
soma = [[0 for j in range(len(matriz[0]))] for i in range(len(matriz))]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        soma[i][j] = matriz[i][j] + oposto[i][j]

# Exibindo a soma da matriz original com a matriz oposta
print("\nA + (-A):")
for linha in soma:
    print(linha)

#5)gere a matriz transposta dela At
A = [[-7, 8],
    [4, 9],
    [2, 1]
    ]
At = [[0 for j in range(len(A))] for i in range(len(A[0]))] #As dimensões são invertidas, ou seja, o número de linhas de At é igual ao número de colunas de A e vice-versa.
# Preenchendo a matriz transposta
for i in range(len(A)): #Um loop aninhado percorre cada elemento da matriz original A e coloca o elemento na posição correspondente na matriz transposta 𝐴𝑡
    for j in range(len(A[0])):
        At[j][i] = A[i][j]
# Exibindo a matriz transposta
print("\nMatriz transposta At:")
for linha in At:
    print(linha)

#6)Dada as matrizes A e B determine A × B.
A = [[2, 3, 1],
    [-1, 0, 2]
    ]

B = [[1, -2],
    [0, 5],
    [4, 1]
    ]

# Criando a matriz resultante C com zeros
C = [[0, 0], [0, 0]]  # Inicializando C como uma matriz 2x2

# Multiplicando A e B
for i in range(2):  # Para cada linha de A
    for j in range(2):  # Para cada coluna de B
        # Multiplicando os elementos e somando
        C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + A[i][2] * B[2][j]

# Exibindo a matriz resultante
print("Matriz C (Resultado de A * B):")
for linha in C:
    print(linha)

# #7)matriz identidade
n = int(input("Informe a ordem da matriz identidade: "))

# Criar a matriz identidade
identidade = [[0 for j in range(n)] for i in range(n)]  # Inicializa uma matriz n x n com zeros

# Preencher a matriz identidade
for i in range(n):
    identidade[i][i] = 1  # Define a diagonal principal como 1

# Exibir a matriz identidade
print("Matriz identidade de ordem", n, ":")
for linha in identidade:
    print(linha)


#9.1)Faça um programa que leia a matriz anterior e informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas;]
matriz_t = [
    [0, 2, 11, 6, 15, 11, 1],
    [2, 0, 7, 12, 4, 2, 15],
    [11, 7, 0, 11, 8, 3, 13],
    [6, 12, 11, 0, 10, 2, 1],
    [15, 4, 8, 10, 0, 5, 13],
    [11, 2, 3, 2, 5, 0, 14],
    [1, 15, 13, 1, 13, 14, 0]
    ]

# Função para consultar o tempo entre duas cidades
def consultar_tempo(cidade1, cidade2):
    return matriz_t[cidade1 - 1][cidade2 - 1]

# Exemplo de entrada do usuário
cidade1 = int(input('Informe a primeira cidade (1-7): '))
cidade2 = int(input('Informe a segunda cidade (1-7): '))

# Exibir o tempo entre as cidades
tempo = consultar_tempo(cidade1, cidade2)
print(f"O tempo necessário para percorrer entre as cidades {cidade1} e {cidade2} é: {tempo} horas.")


#9.2)Faça um programa que permita ao usuário informa várias cidades e as armazene no vetor de rota até que ele informe 0 (zero), após isto imprima o tempo total para cumprir todo o trajeto fornecido passando por todas as cidades.
# Função para calcular o tempo total de uma rota
def calcular_tempo_total(rota):
    tempo_total = 0
    for i in range(len(rota) - 1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i + 1]
        tempo_total += consultar_tempo(cidade_atual, proxima_cidade)
    return tempo_total

# Permitir ao usuário inserir uma sequência de cidades
rota = []
while True:
    cidade = int(input("Informe uma cidade para adicionar à rota (1-7) ou 0 para finalizar: "))
    if cidade == 0:
        break
    rota.append(cidade)

# Exibir a rota escolhida
print("A rota escolhida foi:", rota)

# Calcular e exibir o tempo total
tempo_total = calcular_tempo_total(rota)
print(f"O tempo total para percorrer a rota é: {tempo_total} horas.")


#10)Implemente um programa que exiba um triângulo de Pasca
# Função para gerar o Triângulo de Pascal de ordem n
def gerar_triangulo_pascal(n):
    # Inicializando a matriz quadrada de ordem n com zeros
    matriz = [[0 for j in range(n)] for i in range(n)]
    
    # Preenchendo a primeira coluna e a diagonal principal com 1
    for i in range(n):
        matriz[i][0] = 1  # Primeira coluna
        matriz[i][i] = 1  # Diagonal principal

    # Preenchendo os demais elementos da matriz
    for i in range(2, n):  # Inicia na linha 2, pois as duas primeiras linhas são triviais
        for j in range(1, i):  # Preenchendo até a diagonal principal
            matriz[i][j] = matriz[i-1][j] + matriz[i-1][j-1]  # Soma do elemento acima com o vizinho da esquerda

    # Exibir a matriz de forma triangular
    for i in range(n):
        for j in range(i+1):  # Exibir até a diagonal principal
            print(matriz[i][j], end="\t")
        print()  # Nova linha após cada linha do triângulo

# Solicitar a ordem do triângulo de Pascal ao usuário
ordem = 7  # Exemplo de ordem (pode ser alterado)

# Gerar e exibir o Triângulo de Pascal
gerar_triangulo_pascal(ordem)


# #Inicialização da matriz:A matriz quadrada de ordem n é criada, onde todas as posições são inicialmente preenchidas com 0.Preenchimento da primeira coluna e da diagonal principal:
# Todos os elementos da primeira coluna (matriz[i][0]) e da diagonal principal (matriz[i][i]) são preenchidos com 1, conforme a regra do Triângulo de Pascal.
# Preenchimento dos outros elementos:

# Para os elementos restantes, cada posição matriz[i][j] é a soma do elemento acima (matriz[i-1][j]) com o vizinho à esquerda (matriz[i-1][j-1]).
# Exibição do triângulo:

# O código exibe apenas os elementos até a diagonal principal em cada linha, formando o triângulo.