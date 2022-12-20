"""
Na matemática, a conjectura de Collatz diz respeito à sequências finitas definidas por um número inteiro 
positivo N. Dado esse N, cada termo desta sequência é obtido do termo anterior da seguinte forma: se o 
termo anterior for par, o próximo termo da sequência será a metade do anterior (N/2). Caso o termo anterior 
seja ímpar, o próximo será 3 vezes o termo anterior mais 1 (3N+1). Pela conjectura de Collatz assume-se que,
 independente do valor de N, a sequência sempre alcançará o valor 1. Diante disso, escreva um programa que 
 simule a conjectura de Collatz, utilizando um laço while. Para cada número da sequência, imprima a sua 
 quantidade em ‘#’. Por exemplo, para o número 6 seriam impressos seis #: ######.

Caso um valor de entrada inválido seja fornecido, seu programa deve acusar uma mensagem de erro "Entrada inválida".  

Input

A entrada consiste em um único número inteiro indicando o termo inicial da sequência.

Output

A saída deve imprimir cada um dos demais termos da sequência até seu fim quando o valor de N é igual 1, sempre imprimindo uma tabulação (\t) e o número equivalente de #s para cada termo.  

Samples Input	Samples Output

16
Conjectura de Collatz para N = 16
8    ########
4    ####
2    ##
1    #

42
Conjectura de Collatz para N = 42
21   #####################
64   ################################################################
32   ################################
16   ################
8    ########
4    ####
2    ##
1    #

12
Conjectura de Collatz para N = 12
6    ######
3    ###
10   ##########
5    #####
16   ################
8    ########
4    ####
2    ##
1    #

3
Conjectura de Collatz para N = 3
10   ##########
5    #####
16   ################
8    ########
4    ####
2    ##
1    #

-1
Entrada inválida

X
Entrada inválida
"""

try:
    N = int(input())

    if N <= 1:
        print("Entrada inválida")

    else:
        print(f"Conjectura de Collatz para N = {N}")
        while N!=1:
            if N%2 == 0:
                N = int(N/2)
                print(f"{N}\t","#"*N)
                #print(f"{str(N).ljust(4,' ')}","#"*N)
            else:
                N = int(3*N+1)
                print(f"{N}\t","#"*N)
except:
    print("Entrada inválida")
