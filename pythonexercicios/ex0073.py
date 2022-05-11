tabela = ('corinthians',
          'Atlético - mg',
          'Internacional',
          'Bragantino',
          'Palmeiras',
          'Flamengo',
          'Sao Paulo',
          'Santos',
          'Fluminense',
          'Coritiba',
          'América - mg',
          'Botafogo',
          'Cuiaba',
          'Ceara SC',
          'Avai',
          'Atletico - PR',
          'Goias',
          'Atlético - GO',
          'Fortaleza')

print('Os primeiros 5 colocados são:')
print('----------------------------')
for c in range (0,5):
    print(tabela[c])
print('Os ultimos 4 colocados são:')
print('----------------------------')
for c in range (15,19):
    print(tabela[c])
print('Todos os times em ordem alfabetica são')
print('-----------------------------')
print(sorted(tabela))


