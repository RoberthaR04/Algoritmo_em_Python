def conceito(nota):
    if nota >=9 and nota <=10:
        return "A"
    elif nota >=8:
        return "B"
    elif nota >=7:
        return "C"
    elif nota >=6:
        return "D"
    else:
        return "F"

nota=float(input('Informe a nota: '))
final=conceito(nota)
print ('Conceito do estudante é:', final)