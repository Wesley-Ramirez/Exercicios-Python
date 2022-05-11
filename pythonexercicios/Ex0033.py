s = int(input('Digite seu salarío '))
base = 1250
if s > base:
    print('Seu novo salario é de {} R$'.format(s * 1.1))
else:
    print('Seu novo salario é de {} R$'.format(s * 1.15))