
def validador(x):
    cont=0
    for i in x:
        if i in('1','2','3','4','5','6','7','8','9','0'):
            cont=cont+1
    if cont == 11 and len (x) == 11:
       return 'É um cpf'
    elif x[3]=='.' and x[7]=='.' and x[11]=='-' and cont == 11 and len (x) == 14:
       return 'É um cpf'
    
    else:
    
      return 'Não é um cpf'
x=str(input('Informe CPF:'))
print(validador(x))
