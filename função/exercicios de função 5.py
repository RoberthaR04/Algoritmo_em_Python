def classe(idade):
    if idade < 16:
        return "Não eleitor"
    elif (idade >=16 and idade <18) or idade >=65:
        return "Eleitor facultativo"
    else:
        return "Eleitor obrigatório"
idade=int(input('Informe a idade: '))
elitor=classe(idade)
print('Sua classe é de:', elitor)