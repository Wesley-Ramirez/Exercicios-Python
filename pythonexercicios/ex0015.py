dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foi rodado? '))
tot = (dias * 60) + (km * 0.15)
print('O total a ser pago é de {} R$'.format(tot))