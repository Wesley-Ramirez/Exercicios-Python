peso = float(input('Digite seu peso em Kg'))
altura = float(input('Digite sua altura em Metros'))
IMC =peso / ( altura * altura )
if IMC < 18.5:
    print('Seu IMC é {},voce esta abaixo do peso ideal'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('Seu IMC é {} , Voce esta no peso ideal'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('Seu IMC é {}, Voce esta com sobrepeso'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('Seu IMC é {}, Voce esta com obesidade'.format(IMC))
elif IMC >= 40:
    print('Seu IMC é {}, Voce esta com obesidade Mórbida.'.format(IMC))
