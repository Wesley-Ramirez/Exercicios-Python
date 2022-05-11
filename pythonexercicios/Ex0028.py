import random
random.seed()
sorteio = random.randint(1,5)
n = int(input('Digite um numero de 1 a 5 '))
if n == sorteio:
    print('Parabéns , voce acertou')
else:
    print('Tente novamente.')


