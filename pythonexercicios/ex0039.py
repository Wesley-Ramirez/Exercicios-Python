ano = int(input('Qual ano que voce nasceu?'))
idade = 2022 - ano
if idade < 18:
    print('Voce tem {} anos , ainda vai se alistar!'.format(idade))
    print('Faltam {} anos para voce se alistar'.format(18 - idade))
elif idade == 18:
    print('Voce tem {} anos , esta na hora de se alistar!'.format(idade))
else:
    print('Voce tem {} anos , já passou da hora de voce se alistar!'.format(idade))
    print('Ja se passaram {} anos desde a data do alistamento'.format(idade - 18))
