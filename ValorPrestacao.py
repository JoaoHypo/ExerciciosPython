'''
Valor da prestação

Faça um programa com uma função que tenha como argumentos o valor de uma prestação e o número de dias em atraso. Esta função deve retornar o valor a ser pago após multas e juros em caso de atraso. O cálculo do valor a ser pago é feito da seguinte forma:
Para pagamentos sem atraso, cobrar o valor da prestação.
Para pagamentos com atraso, cobrar 2% de multa, mais 0,5% de juros por dia de atraso, usando juros simples.
Após a execução da função, o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as declarações e chamadas de funções foram implementadas corretamente de acordo com o que pede o enunciado.  
Input
O valor da prestação e o número de dias em atraso (um por linha), até que seja informado um valor de prestação igual a zero.
Output
Valor final da prestação após multas e juros, em caso de atraso.
Samples Input	Samples Output
300
0
0
300.00
528
10
0
564.96
100
1
500
0
0
102.50
500.00
'''

while True:
    v = int(input())
    if v == 0: break
    d = int(input())

    def prestacao(v,d):
        if d > 0:
            vf = v + (v*0.02) + (v*(d*0.005))
        else:
            vf = v
        return vf

    print(f'{prestacao(v,d):.2f}')