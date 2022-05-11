d = int(input('Digite a distancia da tua viagem(Km)'))
if d <= 200:
    print('Voce terá de pagar {} R$'.format(d * 0.5))
else:
    print('Voce terá de pagar {} R$'.format(d * 0.45))

