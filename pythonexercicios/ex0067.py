n = c = 0
while n >= 0:
    n = int(input('Digite o numero da tabuada!! '))
    if n < 0 :
        break
    for c in range (0,11):
        print(f'{n} X {c} = {n * c}')
    c += 1

