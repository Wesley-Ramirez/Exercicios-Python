import random
def sorteia():
    for c in range (1,6):
        numeros.append(random.randint(0,10))
def somapar():
    for valor in numeros:
        if valor % 2 == 0:
            soma.append(valor)
    print(f'os numeros pares sorteados foram {soma} , e a soma deles é {sum(soma)}')


numeros = list()
soma = list()
sorteia()
print(numeros)
somapar()