import random
random.seed()
c = 0
sorteio = random.randint(0,10)
n = int(input('Digite um numero de 0 a 10 '))
while sorteio != n:
    print('Voce errou , tente novamente!!')
    n = int(input('Digite um numero de 0 a 10 '))
    c = c + 1
print('Voce precisou de {} palpites para acertar'.format(c))
