f = int(input('Digite o numero a ser fatorado '))
c = f
while c > 1:
    c = c - 1
    f = f * c
print('O resultado do numero fatorial é {}'.format(f))