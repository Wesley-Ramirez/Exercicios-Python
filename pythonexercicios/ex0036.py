valor = float(input('Qual é o valor da casa ?'))
salario = float(input('Qual é o seu salario atual?'))
anos = int(input('Quantos anos voce quer pagar?'))
prestaçao = valor / (anos * 12)
if prestaçao >= salario * 0.3:
    print('Sua prestação é de {}, infelizmente o emprestimo foi RECUSADO'.format(prestaçao))
else:
    print('Sua prestação é de {} , seu emprestimo foi aprovado.'.format(prestaçao))