c = 0
media = 0
maior = 0
menor = 1000
r = str()
while r != 'N':
    n1 = int(input('Digite um numero!!'))
    c = c + 1
    media = media + n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    r = str.upper(input('Deseja continuar? [S/N]'))
print('A média de todos numeros digitados foi {}'.format(media / c))
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))



