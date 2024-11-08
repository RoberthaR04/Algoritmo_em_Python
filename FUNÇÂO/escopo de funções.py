x= 0 #variável global, pois foi declarada fora da função

def keyPressed():
    #queremos alterar o valor da variável global x.
    global x
    x= x+1
    print(x)

def calcular_desconto(valor, desconto):
    vlr_desconto = valor*desconto/100
    return vlr_desconto