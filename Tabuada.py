'''
Tabuada

Faça um programa que calcule a tabuada de um número fornecido pelo usuário (o multiplicando). O programa deve conter uma função que tenha como argumento obrigatório o multiplicando, e como argumentos opcionais um valor inicial e um valor final para o multiplicador. A função deve montar e imprimir (na própria função) a tabuada do multiplicando iniciando pelo valor inicial até o valor final do multiplicador. Caso o valor inicial e final do multiplicador não forem informados, a tabuada deve começar em 1 e terminar em 10. Caso apenas o valor final do multiplicador seja informado, a tabuada deve iniciar em 1 e ir até o valor final. Caso apenas o valor inicial do multiplicador seja informado, a tabuada deve iniciar no valor inicial e ir até 10 . Em qualquer caso que o valor de inicial seja maior que o valor final, o programa deve imprimir a mensagem "Entrada inválida". A entrada de dados deve ser feita no programa principal.
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as declarações e chamadas de funções foram implementadas corretamente de acordo com o que pede o enunciado.
Input
A entrada consiste em três linhas.
Na primeira linha o valor do multiplicando.
Na segunda linha, o valor inicial opcional.
Na terceira linha, o valor final opcional.
Output
A saída deve conter uma operação por linha. Com a seguinte forma: multiplicando x valor = resultado.
Samples Input	Samples Output
5


5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5
20
25
5 x 20 = 100
5 x 21 = 105
5 x 22 = 110
5 x 23 = 115
5 x 24 = 120
5 x 25 = 125
8

6
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
6
-10
0
6 x -10 = -60
6 x -9 = -54
6 x -8 = -48
6 x -7 = -42
6 x -6 = -36
6 x -5 = -30
6 x -4 = -24
6 x -3 = -18
6 x -2 = -12
6 x -1 = -6
6 x 0 = 0
5
10
5
Entrada inválida
9
2

9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 9

'''
def tabuada(multiplicando, inicio=1, fim=10):
    if inicio > fim:
        print("Entrada inválida")
    else:
        for i in range(inicio, fim+1):
            print(f"{multiplicando} x {i} = {multiplicando*i}")

multiplicando = int(input())
inicio = input()
fim = input()

if inicio and fim:
    tabuada(multiplicando, int(inicio), int(fim))
elif inicio:
    tabuada(multiplicando, int(inicio))
elif fim:
    tabuada(multiplicando, fim=int(fim))
else:
    tabuada(multiplicando)
