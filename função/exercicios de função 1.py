def enconte_maior_valor(valor1, valor2, valor3):#nome da função depois de def
    
    if valor1 >= valor2 and valor1 >=valor3:
        return valor1
    elif valor2 >= valor1 and valor2 >=valor3:
        return valor2
    elif valor3 >= valor1 and valor3 >=valor2:
        return valor3
v1=int(input('Informe um valor: '))#v1 é um argumento
v2=int(input('Informe um valor: '))
v3=int(input('Informe um valor: '))

maior=enconte_maior_valor(v1,v2,v3)
print(maior)


#ou como eu havia feito antes 
def enconte_maior_valor(valor1, valor2, valor3):#nome da função depois de def
    return max(valor1, valor2, valor3) #return é opicional, porém quase sempre retorna à algo
v1= float(input('Informe um valor: '))
v2= float(input('Informe um valor: '))
v3= float(input('Informe um valor: '))

vmaior= enconte_maior_valor(v1, v2, v3)
print(f'O valor maior é:{vmaior}')