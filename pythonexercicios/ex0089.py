boletin = dict()
boletin['nome'] = str(input('Nome: '))
boletin['Média'] = float(input(f'Média de {boletin["nome"]} '))
if boletin['Média'] < 7:
    boletin['Situação'] = 'Reprovado'
else:
    boletin['Situação'] = 'Aprovado'
for k , v in boletin.items():
    print(f'{k} é igual a {v}')