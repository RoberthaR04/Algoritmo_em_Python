from sys import exit #não sei o que é 

def morrer(motivo):
    print(motivo, "Que vacilo!")#quando morrer vai aparecer isso
    exit(0)

def batcaverna():#função adicionada 
    print("Você entrou na Batcaverna cheia de ouro, joias e umas bugigangas mágicas.")
    print("Tem uma inscrição na parede que diz: 'Leve só o que precisa, ou os guardiões vão ficar pistolas. Que coisa não?'.")
    print("Quanto ouro você vai pegar?")
    escolha = input("> ")
    
    try:
        quanto = int(escolha)
    except ValueError:
        morrer("Isso nem é um número, mano! Os guardiões não perdoam vacilo!")

    if quanto <= 50: #jeito mais fácil de digitar número 
        print("Boa! Você pegou só o necessário. Os guardiões até deram um sorrisinho.")
        print("Uma aura de proteção te envolve. Parabéns, você zerou o jogo e encontrou o Quico!")
        exit(0)
    elif 50 < quanto <= 100:
        print("Você pegou bastante, mas ainda tá no limite do aceitável.")
        print("Os guardiões tão de olho... mas você conseguiu sair com o Quico e a bola quadrada!")
        exit(0)
    else:
        morrer("A ganância te dominou! Os guardiões ficaram brabos e você foi amaldiçoado.")

def acapulco():
    print("Você chegou em Acapulco, solzão, praia e muita energia.")
    print("Sua missão é achar o Quico pra devolver a bola quadrada dele.")
    print("Diz a lenda que ele foi visto em Springfield.")
    print("O que você vai fazer?")
    print("Opção A: Procurar pistas na praia.")#adicionamos opções como letras para facilitar na resposta
    print("Opção B: Dar um pulo no hotel onde ele costuma ficar.")
    
    escolha = input("> ")
    
    if escolha.lower() == "a":
        print("Mandou bem! Uma criança na praia viu o Quico pegando um ônibus pra Springfield.")
        springfield()
    elif escolha.lower() == "b":
        print("No hotel, o recepcionista disse que o Quico saiu e foi direto pra Springfield.")
        springfield()
    else:
        morrer("Você ficou enrolando e o Quico se perdeu ainda mais. Fim de jogo.")

def springfield():
    print("Você chegou em Springfield, onde a galera tem sangue amarelo, acredita?")
    print("Na entrada da cidade tem um portão meio sinistro. Pra passar, você precisa resolver uma charada.")
    print("Charada: 'O que sobe e desce sem sair do lugar?'")
    print("Opção A: Elevador")
    print("Opção B: Escada")
    print("Opção C: Temperatura")
    
    escolha = input("> ")
    
    if escolha.lower() == "b":
        print("Certinho! O portão mágico se abriu e você entrou em Springfield.")
        print("Lá dentro, você descobre que o Quico foi visto em Scranton.")
        scranton()
    elif escolha.lower() == "a":
        morrer("Errado! O portão ficou trancado e você foi mandado direto pra Prisão.")
    elif escolha.lower() == "c":
        morrer("Errado! O portão ficou trancado e você foi mandado direto pra Prisão.")
    else:
        exit()

def scranton():
    print("Você chegou em Scranton, a cidade famosa por sua população.") 
    print("Pra descobrir onde tá o Quico, você vai ter que encarar um desafio.")
    print("Opção A: Participar de um concurso de vendas na Dunder Mifflin.")
    print("Opção B: Competir num quiz sobre papel.")
    
    escolha = input("> ")
    
    if escolha.lower() == "a":
        print("Você mandou bem nas vendas e ganhou uma informação importante!")
        print("Descobriu que o Quico foi pra Vila Sésamo.")
        vila_sesamo()
    elif escolha.lower() == "b":
        morrer("Você foi mal no quiz e acabou expulso da cidade. Fim de jogo.")
    else:
        morrer("Você enrolou tanto que te acharam suspeito e te mandaram pra Prisão.")

def vila_sesamo():
    print("Você chegou na Vila Sésamo, onde tudo é colorido e os moradores são super gente boa.")
    print("Pra conseguir ajuda aqui, você precisa dar uma mão pra galera.")
    print("Opção A: Ajudar o Garibaldo a achar as penas dele.")
    print("Opção B: Ajudar o Come-Come a assar biscoitos.")
    
    escolha = input("> ")
    
    if escolha.lower() == "a":
        print("Você ajudou o Garibaldo e, de agradecimento, ele te contou que o Quico tá em Torres Tortas!")
        torres_tortas()
    elif escolha.lower() == "b":
        morrer("Você queimou os biscoitos e o Come-Come ficou bolado, te expulsando da Vila Sésamo. Fim de jogo.")
    else:
        morrer("Você enrolou e perdeu a chance de conseguir informações. Fim de jogo.")

def torres_tortas():
    print("Finalmente, você chegou em Torres tortas, que fica bem no meio do mapa.")
    print("A cidade é linda e cheia de magia.")
    print("Aqui, você vai ter que encarar um último desafio pra encontrar o Quico.")
    print("Opção A: Resolver um enigma antigo.")
    print("Opção B: Encarar um guardião místico num duelo de inteligência.")
    
    escolha = input("> ")
    
    if escolha.lower() == "a":
        print("Enigma: 'Tenho cidades, mas não casas. Tenho montanhas, mas não árvores. Tenho água, mas não peixes. O que sou eu?'")
        print("Opção A: Mapa")
        print("Opção B: Globo")
        print("Opção C: Paisagem")
        
        resposta = input("> ")
        
        if resposta.lower() == "a":
            print("Mandou bem! Você resolveu o enigma e o Quico apareceu, agradecido pela sua ajuda.")
            print("Você entrega a bola quadrada pro Quico e ele te leva pra Batcaverna")
            batcaverna()
        else:
            morrer("Errou! Você falhou no desafio final. Fim de jogo.")
    elif escolha.lower() == "b":
        print("O guardião místico te desafia com a seguinte pergunta:")
        print("'Qual número falta na sequência: 2, 3, 5, 7, 11, ?'")
        print("Opção A: 13")
        print("Opção B: 14")
        print("Opção C: 15")
        
        resposta = input("> ")
        
        if resposta.lower() == "a":
            print("Acertou! O guardião te reconhece como inteligente e deixa você encontrar o Quico.")
            print("Você entrega a bola quadrada pra ele e vai direto pra sala do tesouro.")
            batcaverna()
        else:
            morrer("Errou! O guardião te baniu de Torres Tortasb. Fim de jogo.")
    else:
        morrer("Você demorou demais e perdeu a chance de encontrar o Quico. Fim de jogo.")

def prisao():#adicionamos uma prisão
    print("Você tá na Prisão, um lugar sinistro onde ficam os que fracassaram nos desafios.")
    print("Pra escapar, você vai ter que encarar um desafio arriscado.")
    print("Opção A: Enganar o guarda com uma história convincente.")
    print("Opção B: Encontrar uma passagem secreta cavando a parede.")
    
    escolha = input("> ")
    
    if escolha.lower() == "a":
        print("Sua história foi tão boa que o guarda te soltou!")
        print("Você decide voltar pra Acapulco e recomeçar a jornada.")
        acapulco()
    elif escolha.lower() == "b":
        morrer("Te pegaram cavando e aumentaram sua sentença. Fim de jogo.")
    else:
        morrer("Você não se decidiu e ficou preso pra sempre. Fim de jogo.")

def iniciar():#mudamos o nome da cidade
    print("Bem-vindo à sua grande aventura!")
    print("Sua missão é encontrar o Quico e devolver a bola quadrada dele.")
    print("Sua jornada começa em Acapulco.")
    acapulco()

# Início do jogo
iniciar()
