n = cont = soma = 0
while n != 999:
    n = int(input('Digite um numero!! '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce digitou {cont} numeros , e a soma de todos eles é {soma}')