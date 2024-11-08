salario= float(input('Informe o valor do seu salário: R$'))
desp_agua=float(input('Informe o valor da conta de Água: R$'))
desp_energ=float(input('Informe o valor da conta de Energia: R$'))
desp_int= float(input('Informe o valor da conta de Internet: R$'))
desp_alug=float(input('Informe o valor do Aluguel: R$'))
desp_adc= float(input('Informe o valor de outros gastos adicionais: R$'))

total_desp= (desp_agua+desp_adc+desp_alug+desp_int+desp_energ)
resto_salario = (salario - total_desp)
print('\nO valor total das despesas é R${:.2f}'.format(total_desp))
print('\nO que sobrou do salário após retirar o valor das despesas foi R${:.2f}'.format(resto_salario))

simulador = int(input('\nDeseja simular quantos por cento pode economizar esse mês? \nPara SIM Digite(1) \nPara NÃO Digite(2) \n\nEscolha uma opção: '))

if simulador == 1:
      print('\nDigite um número de acordo com as Opções: ')
      for i in range(1,100):
          escolha=int(input('\n 1- 10%\n 2- 20%\n 3- 30%\n 4- Para escolher a porcentagem\n 5- Sair \n\nEscolha uma opção: '))
          if escolha == 1:
                porcentagem = 10
          elif escolha == 2:
                porcentagem = 20
          elif escolha == 3:
                porcentagem = 30
          elif escolha == 4:
                porcentagem = float(input('\nInforme a porcentagem que você gostaria de economizar do salário após as despesas: '))
          elif escolha == 5:
                print('Até a próxima!')
                break
          else:
                print('Não existe essa opção!')
                porcentagem = 0

          if porcentagem > 0:
                v_economia = resto_salario * (porcentagem /100)//1
                resto = (resto_salario - v_economia)*(1)//1
                print('\nA porcentagem que será economizada:',porcentagem,'%')
                print('O valor que deverá ser economizado: R${:.2f}'.format(v_economia))
                print('O valor exedente é de R${:.2f}'.format(resto))
                o = int(input('\nGostaria de ver quanto renderia por mês na poupança se guardasse R${:.2f} todos os meses rendendo 0,5% no periodo de 1 ano? Digite: \n1 Para Sim \n2 Para Não \n\n Escolha uma opção: '.format(v_economia)))
                if o == 1:
                      e = v_economia
                      for b in range(1,2):
                            print('\nMês', b)
                            v_economia += v_economia * 0.005
                            print('R${:.2f}'.format(v_economia))
                            for a in range(2,12+1):
                                  print('\nMês', a)
                                  v_economia += e
                                  v_economia += v_economia * 0.005
                                  print('R${:.2f}'.format(v_economia))
                      print('\nValor após um ano R${:.2f}'.format(v_economia))

                voltar = int(input('\nDeseja escolher outra opção de porcentagem? Digite: \n1 Para Sim \n2 Para Não \n\n Escolha uma opção: '))
                if voltar == 2:
                       print('\nObrigado por utilizar o simulador. Até a próxima!')
                       break
else:
      print('Obrigado por utilizar o simulador. Até a próxima!')
