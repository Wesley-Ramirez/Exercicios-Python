n = []
for c in range (0,5):
    n.append(int(input('Digite um Numero!! ')))
print(f'O maior numero digitado foi {max(n)}, e o menor numero digitado foi {min(n)}')
print(f'O maior foi digitado na posição {n.index(max(n))} e o menor na posição {n.index(min(n))}')