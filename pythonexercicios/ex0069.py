maioridade = homens = mulheres = 0
r = str()
while r != 'N':
    idade = int(input('Digite sua idade!! '))
    sexo = str(input('Digite seu sexo [M/F]').upper())
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20 :
        mulheres += 1
    r = str(input('Deseja continuar?[S/N]').upper())
print(f'No total , tem {maioridade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens no total')
print(f'No total , foram cadastradas {mulheres} mulheres com menos de 18 anos.')

