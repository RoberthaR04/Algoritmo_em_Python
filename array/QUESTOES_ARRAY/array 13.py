#Função do programa
def eleicao():
    #Solicita o número de candidatos e votantes
    num_candidatos = int(input("Digite o número total de candidatos: "))
    num_votantes = int(input("Digite o número total de votantes: "))

    #Inicia o vetor de votos com zeros com um elemento para cada candidato
    votos = [0] * num_candidatos

    #Coletando os votos dos votantes
    for i in range(num_votantes):
        voto = int(input(f"Votante {i+1}, escolha o número do seu candidato (1 a {num_candidatos}): "))

        #Verificação do voto
        if 1 <= voto <= num_candidatos:
            votos[voto - 1] += 1  #Incrementa o voto ao candidato
        else:
            print("Voto inválido! Tente novamente.")
            i -= 1 #Decrementa o contador para repetir a votação desse votante

    #Mostrando o número de votos de cada candidato
    for i in range(num_candidatos):
        print(f"Candidato {i+1} recebeu {votos[i]} votos.")

#Chamando a função
eleicao()
