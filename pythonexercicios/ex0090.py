import time
from random import randint
resultados = dict()
jogadores = list()
print('Valores Sorteados:')
for c in range (1,5):
    time.sleep(0.8)
    resultados['Jogador'] = c
    resultados['Valor'] = randint(1,6)
    jogadores.append(resultados.copy())
    print(f'O jogador {c} tirou {resultados["Valor"]}')
print('Ranking Dos Jogadores:')

