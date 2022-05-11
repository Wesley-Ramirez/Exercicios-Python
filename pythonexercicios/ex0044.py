valor = float(input('Digite o valor do produto '))
forma = str(input('dinheiro , cartão , 2x no cartão , 3x !!!!'))
if forma == 'dinheiro':
    print('O valor a ser pago é de {} com 10% de desconto'.format(valor * 0.9))
elif forma == 'cartão':
    print('O valor a ser pago é {} com 5% de desconto'.format(valor * 0.95))
elif forma == '2x no cartão':
    print('O valor a ser pago é de {}'.format(valor))
elif forma == '3x' :
    print('O valor a ser pago é de {} com 20% de juros'.format(valor * 1.2))
