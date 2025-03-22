import numpy as np
import random

# Definir uma semente para reprodutibilidade
np.random.seed(42)
random.seed(42)

# Matriz de distâncias entre 21 cidades (simétrica)
cidades = np.array([
    [0, 19, 17, 34, 7, 20, 10, 17, 28, 15, 23, 29, 23, 29, 21, 20, 9, 16, 21, 13, 12],
    [19, 0, 10, 41, 26, 3, 27, 25, 15, 17, 17, 14, 18, 48, 17, 6, 21, 14, 17, 13, 31],
    [17, 10, 0, 47, 23, 13, 26, 15, 25, 22, 26, 24, 27, 44, 7, 5, 23, 21, 25, 18, 29],
    [34, 41, 47, 0, 36, 39, 25, 51, 36, 24, 27, 38, 25, 44, 54, 45, 25, 28, 26, 28, 27],
    [7, 26, 23, 36, 0, 27, 11, 17, 35, 22, 30, 36, 30, 22, 25, 26, 14, 23, 28, 20, 10],
    [20, 3, 13, 39, 27, 0, 26, 27, 12, 15, 14, 11, 15, 49, 20, 9, 20, 11, 14, 11, 30],
    [10, 27, 26, 25, 11, 26, 0, 26, 31, 14, 23, 32, 22, 25, 31, 28, 6, 17, 21, 15, 4],
    [17, 25, 15, 51, 17, 27, 26, 0, 39, 31, 38, 38, 38, 34, 13, 20, 26, 31, 36, 28, 27],
    [28, 15, 25, 36, 35, 12, 31, 39, 0, 17, 9, 2, 11, 56, 32, 21, 24, 13, 11, 15, 35],
    [15, 17, 22, 24, 22, 15, 14, 31, 17, 0, 9, 18, 8, 39, 29, 21, 8, 4, 7, 4, 18],
    [23, 17, 26, 27, 30, 14, 23, 38, 9, 9, 0, 11, 2, 48, 33, 23, 17, 7, 2, 10, 27],
    [29, 14, 24, 38, 36, 11, 32, 38, 2, 18, 11, 0, 13, 57, 31, 20, 25, 14, 13, 17, 36],
    [23, 18, 27, 25, 30, 15, 22, 38, 11, 8, 2, 13, 0, 47, 34, 24, 16, 7, 2, 10, 26],
    [29, 48, 44, 44, 22, 49, 25, 34, 56, 39, 48, 57, 47, 0, 46, 48, 31, 42, 46, 40, 21],
    [21, 17, 7, 54, 25, 20, 31, 13, 32, 29, 33, 31, 34, 46, 0, 11, 29, 28, 32, 25, 33],
    [20, 6, 5, 45, 26, 9, 28, 20, 21, 21, 23, 20, 24, 48, 11, 0, 23, 19, 22, 17, 32],
    [9, 21, 23, 25, 14, 20, 6, 26, 24, 8, 17, 25, 16, 31, 29, 23, 0, 11, 15, 9, 10],
    [16, 14, 21, 28, 23, 11, 17, 31, 13, 4, 7, 14, 7, 42, 28, 19, 11, 0, 5, 3, 21],
    [21, 17, 25, 26, 28, 14, 21, 36, 11, 7, 2, 13, 2, 46, 32, 22, 15, 5, 0, 8, 25],
    [13, 13, 18, 28, 20, 11, 15, 28, 15, 4, 10, 17, 10, 40, 25, 17, 9, 3, 8, 0, 19],
    [12, 31, 29, 27, 10, 30, 4, 27, 35, 18, 27, 36, 26, 21, 33, 32, 10, 21, 25, 19, 0]
])

# Função para calcular a distância total de uma rota
def calcular_distancia(cidades, rota):
    distancia = 0
    for i in range(len(rota) - 1):
        distancia += cidades[rota[i]][rota[i + 1]]
    distancia += cidades[rota[-1]][rota[0]]  # Fecha o ciclo
    return distancia

# Inicializar uma população aleatória de rotas
def inicializar_populacao(n_cidades, tamanho_populacao):
    return [random.sample(range(n_cidades), n_cidades) for _ in range(tamanho_populacao)]

# Seleção por torneio
def selecionar_pais(populacao, fitness, k=3):
    torneio = random.sample(list(zip(populacao, fitness)), k)
    torneio.sort(key=lambda x: x[1])
    return torneio[0][0]

# Operador de cruzamento (OX)
def cruzamento(pai1, pai2):
    start, end = sorted(random.sample(range(len(pai1)), 2))
    filho = [-1] * len(pai1)
    filho[start:end] = pai1[start:end]
    preenchimento = [gene for gene in pai2 if gene not in filho]
    pos = 0
    for i in range(len(filho)):
        if filho[i] == -1:
            filho[i] = preenchimento[pos]
            pos += 1
    return filho

# Operador de mutação
def mutacao(individuo):
    i, j = random.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

# Algoritmo Genético para resolver o problema do Caixeiro Viajante
def algoritmo_genetico(cidades, n_geracoes, tamanho_populacao, taxa_mutacao):
    n_cidades = len(cidades)
    populacao = inicializar_populacao(n_cidades, tamanho_populacao)
    
    for _ in range(n_geracoes):
        fitness = [calcular_distancia(cidades, rota) for rota in populacao]
        nova_populacao = []
        
        for _ in range(tamanho_populacao):
            pai1 = selecionar_pais(populacao, fitness)
            pai2 = selecionar_pais(populacao, fitness)
            filho = cruzamento(pai1, pai2)
            if random.random() < taxa_mutacao:
                filho = mutacao(filho)
            nova_populacao.append(filho)
        
        populacao = nova_populacao
    
    melhor_rota = min(populacao, key=lambda x: calcular_distancia(cidades, x))
    return melhor_rota, calcular_distancia(cidades, melhor_rota)

# Executar o Algoritmo Genético
melhor_rota, distancia = algoritmo_genetico(
    cidades,
    n_geracoes=300,         # Número de gerações
    tamanho_populacao=50,   # Tamanho da população
    taxa_mutacao=0.1        # Taxa de mutação
)

print(f"Melhor rota encontrada: {melhor_rota}")
print(f"Distância total: {distancia}")
