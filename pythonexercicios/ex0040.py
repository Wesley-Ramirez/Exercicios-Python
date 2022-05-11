n1 = float(input('Digite sua primeira nota !'))
n2 = float(input('Digite sua segunda nota!'))
media = (n1 + n2 ) / 2
if media < 5:
    print('Sua media é de {} , voce foi REPROVADO'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua media é de {}, voce ficou de RECUPERAÇÃO.'.format(media))
else:
    print('Sua media é de {}, voce foi APROVADO.'.format(media))

