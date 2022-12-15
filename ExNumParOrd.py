# LAB04-E - Números pares ordenados

''' 
Escreva um programa que leia 3 números inteiros não repetidos, informados pelo usuário. Seu programa deve ler, identificar e retornar, como saída, apenas os números pares ordenados de forma crescente.   
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se os comandos de seleção foram implementados corretamente.     
Input
Entre com 3 números inteiros (não repetidos).
Output
Apenas os números pares ordenados de forma crescente.
Samples Input, Samples Output
22
21
16

16
22

1
2
3

2
2

4
8
2

4
8

9
4
6

4
6
'''


lista = []

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1%2 == 0:
    lista.append(n1)
if n2%2 == 0:
    lista.append(n2)
if n3%2 == 0:    
    lista.append(n3)

lista.sort()

for i in lista:
    print(i)
    