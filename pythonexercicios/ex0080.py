l = []
n = int()
r = str()
while r != 'N':
    l.append(int(input('Digite um valor!! ')))
    r = str(input('Deseja continuar?[S/N]').upper())
    if r != 'N' and r != 'S':
        r = str(input('Resposta invalida , Deseja continuar?[S/N]').upper())
    elif r == 'N':
        break
print(l)
print(f'Foram adicionados {len(l)} numeros a lista .')
print(f'A lista em ordem decrescente ficou {l.sort(reverse=True)}')
if 5 in l :
    print(f'O valor 5 foi digitado na posição {l.index(5)}')
else:
    print('O valor 5 nao foi digitado na lista.')

