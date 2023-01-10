'''
Primary Arithmetic

Children are taught to add multi-digit numbers from right-to-left one digit at a time.
 Many find the "carry" operation - in which a 1 is carried from one digit position to be 
 added to the next - to be a significant challenge. Your job is to count the number of
  carry operations for each of a set of addition problems so that educators may assess 
  their difficulty.

Input
Each line of input contains two unsigned integers less than 10 digits. The last line 
of input contains 0 0.

Output
For each line of input except the last you should compute and print the number of carry 
operations that would result from adding the two numbers, in the format shown below.


Sample Input	
123 456
555 555
123 594
0 0


Sample Output
No carry operation.
3 carry operations.
1 carry operation.
'''

numeros = []
while True:
    numeros = [(i) for i in input().split()]

    if numeros == ['0','0']:
        break

    carrys = 0


    #todo = selecionar menor numero, é o fator limitante
    for indice,algarismo in reversed(list(enumerate(numeros[0]))):
        if int((numeros[0])[indice]) + int((numeros[1])[indice]) >= 10:
            carrys = carrys + 1

    
    if carrys == 0:
        print('No carry operation.')

    elif carrys == 1:
        print(f'1 carry operation.')

    else:
        print(f'{carrys} carry operations.')
