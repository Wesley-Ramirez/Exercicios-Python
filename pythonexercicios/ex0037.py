numero = int(input('Digite um numero qualquer'))
base = int(input('Qual base de conversão voce quer ?1(Binarias), 2(octal) e 3(hexadecimal)'))
if base == 1:
    print("O numero em binarios fica {}".format(bin(base)))
elif base == 2:
    print('o numero em octal fina {}'.format(oct(base)))
else:
    print('O numero em hexadecimal fica {}'.format(hex(base)))
