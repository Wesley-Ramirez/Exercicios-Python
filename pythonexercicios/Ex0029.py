v = float(input('Digite a velocidade do carro!'))
m = (v - 80) * 7
if v <= 80:
    print('Voce passou na velocidade permitida')
else:
    print('Voce foi multado , sua multa é de {} R$'.format(m))
