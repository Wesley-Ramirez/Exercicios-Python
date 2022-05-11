n1 = float(input('Digite o primeiro numero '))
n2 = float(input('Digite o segundo numero '))
maior = 0
r = 0
while r != 5:
    print('[1]Somar'
          '\n[2]Multiplicar'
          '\n[3]Maior'
          '\n[4]Novos Numeros'
          '\n[5]Sair do programa')
    r = int(input('Digite sua opção'))
    if r == 1:
        print('A  função somar , resultou em {}'.format(n1 + n2))
    elif r == 2:
        print('A função multiplicar, resultou em {}'.format(n1 * n2))
    elif r == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(maior)
    elif r == 4:
        n1 = float(input('Digite o primeiro novo numero '))
        n2 = float(input('Digite o segundo novo numero '))
    elif r == 5:
        print('Voce saiu do programa')


