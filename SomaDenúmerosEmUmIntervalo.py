'''
Soma de números em um intervalo
Escreva um programa que calcule a soma de números inteiros que estão presentes em um determinado intervalo [A, B], incluindo os valores limites. Por exemplo, a soma dos números inteiros no intervalo [2, 5] é 14 = (2+3+4+5). O programa também deve mostrar o número que divide o intervalo ao meio, caso o tamanho dele seja ímpar, ou os dois números, caso o tamanho do intervalo seja par. Por exemplo, os números que dividem o intervalo [2, 5] são: 3 e 4. O usuário pode informar o intervalo em ordem crescente ou decrescente, ou seja, [2,5] e [5,2] são ambas entradas válidas para a mesma soma.
O somatório deve ser realizado através de laço, ou seja, não utilize formula matemática pronta do somatório.
Input
A entrada consiste em dois valores inteiros indicando os limites do intervalo. Observe que os números podem ser inteiros negativos.
Output
A saída do programa deve apresentar o início do intervalo, o fim do intervalo, o somatório dos inteiros no intervalo, e o(s) valor(es) que representam a metade do intervalo, de acordo com os exemplos abaixo.
Samples Input	
2
6
Samples Output
Início do intervalo: 2
Fim do intervalo: 6
Somatório do intervalo 20
Metade do intervalo 4


-2
-5
Samples Output
Início do intervalo: -2
Fim do intervalo: -5
Somatório do intervalo -14
Metade do intervalo -4 e -3



5
2
Samples Output
Início do intervalo: 5
Fim do intervalo: 2
Somatório do intervalo 14
Metade do intervalo 3 e 4



2
5
Samples Output
Início do intervalo: 2
Fim do intervalo: 5
Somatório do intervalo 14
Metade do intervalo 3 e 4
'''

n1 = int(input())
n2 = int(input())

print(f"Início do intervalo: {n1}")
print(f"Fim do intervalo: {n2}")

if n2 < n1:
    aux = n1
    n1 = n2
    n2 = aux

listavalores = []
soma = 0
for i in range(n1,n2+1): 
    listavalores.append(i)
    soma = soma + i

print(f"Somatório do intervalo {soma}")

lenlista = len(listavalores)

if lenlista%2 == 0:
    limite = int(lenlista/2)
    print(f"Metade do intervalo {listavalores[limite-1]} e {listavalores[limite]}")


else:
    limite = int((lenlista-1)/2)
    print(f"Metade do intervalo {listavalores[limite]}")
