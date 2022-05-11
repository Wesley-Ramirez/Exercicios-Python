import random
random.randint(0,10)
vitorias = soma = c = 0
while c <= 10:
    n1 = int(input('Digite um valor: '))
    escolha = str.upper(input('Voce quér par ou impar? [P/I]'))
    print(f'Voce jogou {n1} e o computador jogou {random.randint(0,10)}')
    if soma %2 ==0 and escolha == 'P':
        print('Parabéns , voce ganhou ')
        c += 1
    elif soma %2 ==1 and escolha == 'P':
        print('Voce Perdeu, GAME OVER.')
        print(f'Voce ganhou {c} vezes seguidas')
        break
    elif soma % 2 == 0 and escolha == 'I':
        print('Voce Perdeu, GAME OVER.')
        print(f'Voce ganhou {c} vezes seguidas')
        break
    elif soma % 2 == 1 and escolha == 'I':
        print('Parabens , voce ganhou ')




