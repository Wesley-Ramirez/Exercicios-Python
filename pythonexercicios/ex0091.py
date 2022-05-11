prev = dict()
prev['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
prev['Idade'] = 2022 - ano
prev['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if prev['CTPS'] == 0:
    for k , v in prev.items():
        print(f'{k} tem o valor {v}')
prev['contratação'] = int(input('Ano de contratação: '))
prev['Salário'] = float(input('Salário: '))
cont = 35 - (2022 - prev['contratação'])
prev['Aposentadoria'] = prev['Idade'] + cont
for k,v in prev.items():
    print(f'{k} tem o valor de {v}')