par = impar = 0
n1 = int(input('Digite o primeiro numero! '))
n2 = int(input('Digite o segundo numero ! '))
n3 = int(input('Digite o terceiro numero !'))
n4 = int(input('Digite o quarto numero !'))
tupla = (n1,n2,n3,n4)
print(tupla)
print(f'O numero 9 apareceu {tupla.count(9)} vezes na tupla')
if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
    print(f'O numero 3 foi digitado na posição {tupla.index(3)}')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
for c in range (0,4):
    if tupla[c] % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print(f'A quantidade de numeros pares foi {par}')
print(f'A quantidade de numeros impares foi {impar}')


