def encontre_perimetro (a,b,c):
    if a<=(b+c) and b<=(a+c) and c<=(b+a):
        lados = a+b+c
        return lados
    else:
        return 'não é triângulo'
lA=float(input('Informe o valor do lado A: '))
lB=float(input('Informe o valor do lado B: '))   
lC=float(input('Informe o valor do lado C: '))

perimetro=encontre_perimetro(lA,lB,lC)
print(perimetro, 'É um triângulo')