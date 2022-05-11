media = 0
qm = 0
hv = 0
nome = ''
for c in range(1,5):
    n = str(input('Digite seu nome!!!'))
    i = int(input('Digite sua idade!!!'))
    s = str(input('masculino ou feminino?'))
    media = media + i
    if c == 1 and s == 'masculino':
        hv = i
        nome = n
    if s == 'masculino' and i > hv:
        hv = i
        nome = n

if s == 'feminino' and i <= 20:
    qm = qm + 1
print('A média das idades é {}'.format(media / 4))
print('O nome do homem mais velho é {} e tem {} anos'.format(nome,hv))
print('O numero de mulheres maiores de 20 anos é {}'.format(qm))

