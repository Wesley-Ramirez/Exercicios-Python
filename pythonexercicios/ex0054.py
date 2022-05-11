maior = 0
menor = 0
for c in range(0,7):
    n = int(input('Digite o ano que voce nasceu!!'))
    idade = 2022 - n
    if idade < 21 :
        menor = menor + 1
    else:
        maior = maior + 1
print('{} Pessoas tem maioridade e {} são menor de idade'.format(maior,menor))

