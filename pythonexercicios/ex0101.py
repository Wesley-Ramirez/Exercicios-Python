def voto(ano):
    global v1
    if idade < 18:
        return 'Voto negado'
    elif idade >= 18 and idade < 65:
        return 'Voto obrigatório'
    else:
        return 'Voto opcional'





ano = int(input('Digite o ano que voce nasceu: '))
idade = 2022 - ano
v1 = voto(ano)
print(f'Com {idade} anos: {v1}')
