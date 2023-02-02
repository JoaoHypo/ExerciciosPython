'''
Palindromo PTBR

Um palíndromo é uma palavra, ou frase, que é igual quando lida da esquerda
para a direita ou da direita para a esquerda (espaços em brancos não são considerados).
Escreva um programa que leia uma string inserida pelo usuário e imprima, como saída,
‘É palíndromo’ caso a string seja um palíndromo e ‘Não é palíndromo’ caso não seja.
Input
Uma string que pode ser ou não um palíndromo.
Output
Uma mensagem indicando se a string informada é ou não um palíndromo.

Samples Input	Samples Output

mega bobagem
É palíndromo

roma
Não é palíndromo

reviver
É palíndromo
'''
string = input()
string = string.split()
result = []

for palavra in string:
    if len(palavra)%2 == 0:
        pass
    else:
        meio = int(len(palavra)/2)
        palavra = palavra[ :meio] + palavra[(meio+1): ]
    normal = []
    reverso = []
    for letra in palavra:
        normal.append(letra)
        reverso.insert(0,letra)
    if normal == reverso:
        pass
    else:
        result.append(0)

if 0 in result:
    print('Não é palíndromo')

else:
    print('É palíndromo')
