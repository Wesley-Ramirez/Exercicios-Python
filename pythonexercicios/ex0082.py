l = []
n = int()
r = str()
par = []
impar = []
while not r == 'N':
    n = int(input('Digite um valor!! ').upper())
    l.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja continuar?[S/N]').upper())
    if r != 'S' and r != 'N':
        r = str(input('Resposta invalida , Deseja continuar?[S/N]').upper())
    elif r == 'N':
        break
print(l)
print(f'Foram Digitados {len(l)} numeros')
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')