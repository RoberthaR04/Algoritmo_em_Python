def aprovacao (totalaulas, nota, faltas):
    if nota >=6 and faltas*100/totalaulas <=25:
        return 1
    else:
        return 0
totalaulas=int(input('Informe o número total de aulas de uma disciplina: '))
nota=float(input('Informe a nota: '))
faltas=int(input('Informe a quantidade de faltas faltas: '))
resul=aprovacao(totalaulas, nota, faltas)


if resul ==1:
    print('Aprovado')
else:
    print('Reprovado')