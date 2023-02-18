# Factor calculator for ax² such as a=1
#Todo = add menu, tipes of factorin, and converstion to fractions! (note: split('/'))

nX = int(input('Digite o termo X: '))
nC = int(input('Digite o termo Cte: '))

print(f'Multiplo 1\tMultiplo2\tCte={nC:.0f}')
for valor in range(-nC,nC+1):
    valor2 = nC/valor
    print(f'{valor}\t\t{valor2}\t\t{nC}')
    if valor2 + valor == nX:
        print(f'The factoring for x² + {nX:.0f}x + {nC:.0f}')
        print(f'is (x + {valor2:.0f}) * (x + {valor:.0f})')
        break
