from random import randint
itens = ('pedra', 'papel' , 'tesoura')
escolha = str(input('Qual voce escolhe? pedra, papel ou tesoura!!!'))
computador = randint(0,2)
if escolha == 'pedra' and computador == 'tesoura':
    print('O computador escolheu {}'.format(computador))
    print('Parabens , voce venceu')
elif escolha == 'papel' and computador == 'pedra':
    print('O computador escolheu {}'.format(computador))
    print('Parabens, voce venceu')
elif escolha == 'tesoura' and computador == 'papel':
    print('O computador escolheu {}'.format(computador))
    print('Parabens, voce venceu')
elif escolha == 'pedra' and computador == 'papel':
    print('O computador escolheu {}'.format(computador))
    print('Voce perdeu')
elif escolha == 'papel' and computador == 'tesoura':
    print('O computador escolheu {}'.format(computador))
    print('Voce perdeu')
elif escolha == 'tesoura' and computador == 'pedra':
    print('O computador escolheu {}'.format(computador))
    print('Voce perdeu')
elif escolha == computador:
    print('O computador escolheu {}'.format(computador))
    print('Deu empate')




