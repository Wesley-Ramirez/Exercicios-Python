lista = []
par = []
impar = []
for c in range (1,8):
    n = int(input(f'Digite o {c}o. valor ! '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista = [par] + [impar]
print(f'Foram digitados os valores {lista}')
par.sort()
impar.sort()
print(f'Em ordem crescente, a lista fica {lista}')
