# Factor calculator for ax² such as a=1

nX = float(input('Digite o termo X: '))
nC = float(input('Digite o termo Cte: '))

print(f'Multiplo 1\tMultiplo2\tCte={nC}')
for valor in range(-nC,nC+1):
    valor2 = nC/valor
    print(f'{valor}\t{valor2}\t{nC}')
    if valor2 + valor == nX:
        pass
