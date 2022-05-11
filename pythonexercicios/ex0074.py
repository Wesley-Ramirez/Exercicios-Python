import random
al = tuple(random.randint(0,11) for c in range(0,5))
print(al)
print(sorted(al))
print(f'O maior valor da tupla é {max(al)}')
print(f'O menor valor da tupla é {min(al)}')


