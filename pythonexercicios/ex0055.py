maior = 0
menor = 500
for c in range(0,5):
    p = float(input('Digite seu peso!!'))
    if p > maior :
        maior = p
    if p < menor:
        menor = p
print('O maior peso digitado foi {} , e o menor foi {}'.format(maior,menor))
