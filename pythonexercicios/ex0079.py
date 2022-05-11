lista =[]
num = int()
r = str()
while r != 'N':
    num = int(input('Digite um valor! '))
    if num in lista:
        print(f'Numero já está na lista')
    else:
        lista.append(num)
    print('Valor adicionado com sucesso!')
    r = str(input('Deseja continuar?[S/N]').upper())
    if r != 'S' and r != 'N':
        r = str(input('Resposta invalida , Deseja continuar? [S/N]'))
    elif r == 'N':
        break
lista.sort()
print(lista)


