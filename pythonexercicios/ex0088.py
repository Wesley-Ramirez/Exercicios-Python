ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Deseja continuar?[S/N]'))
    if resp in 'Nn':
        break
print(f'O aluno {ficha[0]} teve a media {ficha[1]}')
