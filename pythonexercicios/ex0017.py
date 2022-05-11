from math import sqrt
Co = float(input('Digite a medida do cateto oposto '))
Ca = float(input('Digite a medida do cateto adjacente '))
Hip = sqrt(Co * Co + Ca * Ca)
print('A base do triangulo é {} , sua altura é {} e sua hipotenusa é {}'.format(Ca,Co,Hip))
