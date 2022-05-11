dic = dict()
mulheres = list()
r = str()
maioridade =dict()
tudo = list()
tot = media = 0
while r != 'N':
    dic['nome'] = str(input('Nome: '))
    dic['Sexo'] = str(input('Sexo?[M/F] :').upper())
    dic['Idade'] = int(input('Idade :'))
    tudo.append(dic)
    tot = tot + 1
    media = (media + dic['Idade'])
    if dic['Sexo'] == 'F':
        mulheres.append(dic['nome'])
    if dic['Idade'] > media / tot:
            maioridade = dic.copy()
    r = str(input('Deseja continuar?[S/N]').upper())
    if r != 'S' and r != 'N':
        r = str(input('Resposta Invalida , Deseja Continuar?[S/N]').upper())

print(f'O grupo tem {tot} pessoas.')
print(f'A média de idade é de {media / tot} anos. ')
print(f'As mulheres cadastradas foram:{mulheres}')
print(f'Lista das pessoas que estao acima da média:')

for k,v in maioridade.items():
    print(f'{k} = {v}',end='; ')
print('<< ENCERRADO >>')
