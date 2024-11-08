def sauda(nome):
    print('Olá ' + nome + '!')  # Adicionando espaço após 'Olá'
    sauda2(nome)
    print('Preparando para dizer tchau...')
    tchau()

def sauda2(nome):
    print('Como vai ' + nome + '?')  # Adicionando espaço após 'Como vai'

def tchau():
    print('OK, tchau!')  # Corrigindo a digitação de 'tvhau' para 'tchau'

# Chame a função sauda com um nome para ver a saída
nome = input("Informe seu nome: ")
sauda(nome)
