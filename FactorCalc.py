# Factor calculator for ax² such as a=1
#Todo = add menu, tipes of factorin, and converstion to fractions! (note: split('/'))

nX = int(input('Digite o termo X: '))
nC = int(input('Digite o termo Cte: '))

print(f'''\n{'"Brute Force" try process':-^50}''')
print(f'Multiplo 1\tMultiplo2\tSum Expected= {nX:.0f}')

for valor in range(-nC,nC+1):
    valor2 = nC/valor
    print(f'\n{valor:^10.2f}\t{valor2:^10.2f}\t{valor2 + valor:^10.2f}')
    if valor2 + valor == nX:
        print(f'\nThe factoring for x² + {nX:.0f}x + {nC:.0f}')
        print(f'is (x + {valor2:.0f}) * (x + {valor:.0f})\n')
        break
