import time
def contador(inicio,fim, passo):
    for c in range(inicio,fim + 1,passo):
        print(c, end=',')
        time.sleep(0.4)

print('Contagem de 1 até 10 , com passo de 1:')
print('-' * 20)
for c in range (1, 11):
    time.sleep(0.5)
    print(c, end=' ,')
print('\nContagem de 10 até 0 , com passo de 2:')
print('-' * 20)
for c in range (10,0,-2):
    time.sleep(0.5)
    print(c, end=' ,')
print('\nAgora é sua vez de personalizar sua contagem.')
print('-' * 20)
inicio = int(input('Inicio: '))
fim = int(input('FIM: '))
passo = int(input('Passo:'))
if passo == 0:
    passo = 1
contador(inicio,fim,passo)

