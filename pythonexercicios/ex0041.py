ano = int(input('Digite o ano que voce nasceu!'))
idade = 2022 - ano
if idade <= 9:
    print('Voce tem {} anos.'.format(idade))
    print('Voce se enquadra na categoria MIRIM')
elif idade > 9 and idade <= 14 :
    print('Voce tem {} anos.'.format(idade))
    print('Voce se enquadra na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Voce tem {} anos.'.format(idade))
    print('Voce se enquadra na categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Voce tem {} anos.'.format(idade))
    print('Voce se enquadra na categoria SÊNIOR')
else:
    print('Voce tem {} anos.'.format(idade))
    print('Voce se enquadra na categoria MASTER')