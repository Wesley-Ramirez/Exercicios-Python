import random
import time
from random import randint
tot = []
sorteio = []
jogos = int(input('Quantos jogos voce quér que eu jogue? '))
for p in range (1,jogos +1):
    for c in range(0,6):
        sorteio = random.sample(range(0,60),6)
        tot = sorteio[:]
    sorteio.clear()
    time.sleep(0.6)
    tot.sort()
    print(f'Jogo {p}:{tot}')
print('BOA SORTE!!')
