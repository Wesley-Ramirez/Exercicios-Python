def maior(*num):
    print('Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')


maior(0,7,8,9,4,2,6)
print('-' * 20)
maior(0,8,4)
print('-' * 20)
maior(8,9,7,2)




