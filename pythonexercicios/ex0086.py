lista = list()
primeira = []
segunda = []
terceira = []
par = []
n = int()
for c in range (0,3):
    n = int(input(f'Digite um valor para [0,{c}]'))
    if n % 2 == 0:
        par.append(n)
    primeira.append(n)
for c in range (0,3):
    n = int(input(f'Digite um valor para [1,{c}]'))
    if n % 2 == 0:
        par.append(n)
    segunda.append(n)
for c in range (0,3):
    n = int(input(f'Digite um valor para [2,{c}]'))
    if n % 2 == 0:
        par.append(n)
    terceira.append(n)
print('-=' * 30)
print(f'[ { primeira[0] } ]  [ { primeira[1] } ]  [ { primeira[2] } ]')
print(f'[ { segunda[0] } ]  [ { segunda[1] } ]  [ { segunda[2] } ]')
print(f'[ { terceira[0] } ]  [ { terceira[1] } ]  [ { terceira[2] } ]')
print(par)
print(f'A soma dos valores pares é {sum(par)}')
print(f'A soma da terceira coluna é {primeira[2] + segunda[2] + terceira[2]}')
print(f'O maior valor da segunda linha é {max(segunda)}')