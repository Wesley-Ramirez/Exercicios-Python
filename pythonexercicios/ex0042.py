n1 = float(input('Digite a primeira reta!'))
n2 = float(input('Digite a segunda reta!'))
n3 = float(input('Digite a terceira reta!'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2 :
    print('Pode formar um triangulo!')
    if n1 == n2 and n1 == n3:
        print('Este triangulo é EQUILÁTERO')
    elif n1 == n2:
        print('Este triangulo é ISÓSCELES')
    else:
        print('Este triangulo é ESCALENO')
else:
    print('Não pode formar um triangulo!')