'''
Grains in a Chess Board

A queen requested the services of a monk and told him she would pay any price. 
The monk, needing food, asked the queen if the payment could be made in wheat
grains arranged in a chessboard, so that in the first square it would be put
only one grain, and in the subsequent squares twice as much as its previous 
  
Input
The first line of the input contains a single integer N (1 ≤ N ≤ 100), 
indicating the number of test cases. Each test case contains a single integer
X (1 ≤ X ≤ 64), indicating the number of possible squares to be used.

Output
For each test case, print the quantity expected to be received by the monk, 
according to the following example.

Input Sample	
3
7
19
14

Output Sample
0 kg
43 kg
1 kg
'''

tests = int(input())

for i in range(tests):

    quadrados = int(input())
    
    if quadrados > 1:

        soma = 1
        quadrado = 1

        for i in range(quadrados-1):
            quadrado = 2 * quadrado
            soma = soma + quadrado
            pesog = soma/12
            pesokg = (str(pesog/1000)).split('.')

        #print(f'{round(pesog)} g')
        print(f'{pesokg[0]} kg')

    else:
        print('0 kg')
