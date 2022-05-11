produtos = ('Pão',1.0,
            'Leite',3.50,
            'Massa',5.99,
            'Frango',12.00,
            'Carne',35.00,
            'Molho de tomate',1.99,
            'Salgadinho',5.99,
            'Arroz',18.00,
            'Feijão',9.00,
            'Ovo',18.00,
            'Amaciante',25.00,
            'Papel',15.00)
for c in range (0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='') # end para nao quebrar a linha
    else:
        print(f'R${produtos[c]:>4}')#: formata , > alinha 4 numero de casas