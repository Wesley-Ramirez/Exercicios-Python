tentativas = 1
soma = 0
n1 = 0
while n1 != 999:
    n1 = int(input('Digite um numero  '))
    if n1 != 999:
        tentativas = tentativas + 1
        soma = soma + n1
print('Voce parou o programa')
print('Voce fez {} tentativas'.format(tentativas))
print('A soma de todas tentativas foi {}'.format(soma))
