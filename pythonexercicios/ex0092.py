gols = list()
est = {}
est['nome'] = str(input('Nome do Jogador: '))
cont = int(input(f'Quantas partidas {est["nome"]} jogou?'))
for c in range (1,cont + 1):
    gol = int(input(f'Quantos gols na partida {c}?'))
    gols.append(gol)
est['Gols'] = gols
est['total'] = sum(gols)
print(f'O jogador {est["nome"]} jogou {cont} partidas.')
for c in range (0,cont):
    print(f'=> na partida {c},{est["nome"]} fez {gols[c]} gols')
print(f'Foi um total de {sum(gols)} gols.')
