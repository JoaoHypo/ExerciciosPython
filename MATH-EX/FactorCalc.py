# Factor calculator for ax² resulting only in integer factors

#Todo = add menu, tipes of factorin, and converstion to fractions! (note: split('/'))
nX2= int(input('Digite o fator X²: '))
nX = int(input('Digite o faotr X: '))
nC = int(input('Digite o termo C(te): '))
find = False


nX2AUX = nX2*nC
print(f'''\n{'"Brute Force" try process':-^50}''')
print(f'Multiplo 1\tMultiplo2\tSum Expected= {nX:.0f}')

for valor in range(-abs(nX2AUX),abs(nX2AUX+1)):
    if valor == 0:
        continue
    valor2 = nX2AUX/valor
    print(f'\n{valor:^10.2f}\t{valor2:^10.2f}\t{valor2 + valor:^10.2f}')
    if valor2 + valor == nX:
        print(f'\nThe factoring for {nX2:.0f}x² + {nX:.0f}x + {nC:.0f} is: ')
        print(f'(x + {valor2:.0f}) * (x + {valor:.0f})\n'.center(30))
        find = True
        break
if find == False:
    print(f'\nImpossible to factor with integer factors only the expression: {nX2:.0f}x² + {nX:.0f}x + {nC:.0f}')


#Todo? add more cases