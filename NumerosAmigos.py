'''
Números Amigos

Dizemos que dois números são consideramos ‘amigos’ quando se cada um deles é igual à soma dos divisores próprios do 
outro. Os divisores próprios de um número inteiro positivo N são todos os divisores de N exceto o próprio N. 
Por exemplo: 220 e 284 são números amigos pois:
Divisores próprios de 220: 1 2 4 5 10 11 20 22 44 55 e 110 cuja soma é 284.
Divisores próprios de 284: 1 2 4 71 e 142 cuja soma é 220.
Diante disso, crie um programa que receba, como entrada, dois números inteiros positivos N1 e N2 e verifique se 
são números amigos. Seu programa deve mostrar todos os divisores próprios de ambos os números.
Use laço for() para resolver este enunciado.
Input
A entrada consiste em duas linhas, representando os dois números inteiros para os quais deseja-se saber se são amigos.
Output
A saída é composta pela lista de divisores dos números, em seguida a soma dos divisores, e uma mensagem indicando se os
 números são amigos ou não.
Samples Input	
2
6

Samples Output
Divisores próprios de 2: 1 cuja soma é 1
Divisores próprios de 6: 1 2 3 cuja soma é 6
2 e 6 não são amigos



220
230

Divisores próprios de 220: 1 2 4 5 10 11 20 22 44 55 110 cuja soma é 284
Divisores próprios de 230: 1 2 5 10 23 46 115 cuja soma é 202
220 e 230 não são amigos




220
284

Divisores próprios de 220: 1 2 4 5 10 11 20 22 44 55 110 cuja soma é 284
Divisores próprios de 284: 1 2 4 71 142 cuja soma é 220
220 e 284 são amigos

'''
def divisores_proprios(n):

    divisores = []

    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def sao_numeros_amigos(n1, n2):

    divisores_n1 = divisores_proprios(n1)
    divisores_n2 = divisores_proprios(n2)

    soma1 = sum(divisores_n1)
    soma2 = sum(divisores_n2)

    strN1 =""
    strN2 =""

    for i in divisores_n1:
        strN1 = strN1 + " " + str(i)

    for i in divisores_n2:
        strN2 = strN2 + " " + str(i)

    print(f"Divisores próprios de {n1}:{strN1} cuja soma é {soma1}")
    print(f"Divisores próprios de {n2}:{strN2} cuja soma é {soma2}")


    if sum(divisores_n1) == n2 and sum(divisores_n2) == n1:
        print(n1, "e", n2, "são amigos")
    else:
        print(n1, "e", n2, "não são amigos")

n1 = int(input())
n2 = int(input())
sao_numeros_amigos(n1, n2)