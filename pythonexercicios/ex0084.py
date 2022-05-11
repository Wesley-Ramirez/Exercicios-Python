lista = []
dados = []
r = str()
totp = 0
while not r == 'N':
    dados.append(str(input('Digite seu nome!')))
    totp = totp + 1
    dados.append(float(input('Digite seu peso!')))
    lista.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar?[S/N]').upper())
    if r != 'S' and r != 'N':
        r = str(input('Resposta invalida , Deseja continuar?[S/N]?').upper())
print(f'No total, foram cadastrados {totp} pessoas.')

