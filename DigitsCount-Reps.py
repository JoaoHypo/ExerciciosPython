'''
Digits Count

Diana is going to write a list of all positive integers between A and B, inclusive, in base 10 and without any leading zeros. She wants to know how many times each digit is going to be used.

Input
Each test case is given in a single line that contains two integers A and B (1 ≤ A ≤ B ≤ 108). The last test case is followed by a line containing two zeros.
Output
For each test case print a single line with 10 integers representing the number of times each digit is used when writing all integers between A and B, inclusive, in base 10 and without leading zeros. Write the counter for each digit in increasing order from 0 to 9.

Input Sample
1 9
12 321
5987 6123
12345678 12345679
0 0


Output Sample
0 1 1 1 1 1 1 1 1 1
61 169 163 83 61 61 61 61 61 61
134 58 28 24 23 36 147 24 27 47
0 2 2 2 2 2 2 2 1 1
'''

#Criando uma função para devolver uma lista 'dicionário' com pares 
# de tuplas contendo os pares (algarismo,recorrência)
def DigitsCount(a,b):

    count = dict() #Geramos um dicionário

    #Alimentamos o dicionário com os algarismo unitários de 0 a 9 
    #resolve casos que começam depois do zero e antes do 10.
    for i in range(10):  
        count[str(i)] = count.get(i,0)
    
    # Aqui começa a função para o intervalo desejado
    for num in range(a,b+1):

        # Agora separamos os números gerados por algorismos
        for i in str(num):
            algarismos = []
            algarismos.append(i)

            # Por fim realizamos a contagem por meio de métodos de dicionário
            for algarismo in algarismos:
                count[algarismo] = count.get(algarismo,0) + 1

    # Adicionando o resultado em uma lista de tuplas
    result = sorted([(alg,rep) for alg,rep in count.items()])
    return result


# Para inputs em string com valores na mesma string espaçados ex: '12 215'
while True:   

    #Cria uma nova lista puxando os dados da lista split
    numeros =  [int(i) for i in input().split()]
    
    #Fechamos o loop e paramos a contagem
    if numeros == [0, 0]:
        break

    # Aplicamos a função e imprimimos o resultado como o exercício quer
    else:
        result = DigitsCount(numeros[0], numeros[1])  
        finalprint = []
        for alg,rep in result:
            finalprint.append(str(rep))
        print(' '.join(finalprint))
