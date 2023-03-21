'''
Correspondência de dígitos

Construa uma função denominada encaixa que, dados dois argumentos inteiros positivos ‘a’ e ‘b’, verifica se ‘b’ corresponde aos últimos dígitos de ‘a’.  Por exemplo, se a=567890 e b=890, então encaixa. Se a=1243 e b=1243, então encaixa. Se a = 2456 e b=245, então não encaixa. Se a=457 e b=2457, então não encaixa. Usando essa função, faça um programa que lê dois inteiros positivos ‘x’ e ‘y’ e verifica se o menor deles encaixa com o outro. Por exemplo, se x=567890 e y=890, então y encaixa com x. Se x = 1243 e y=221243, então x encaixa com y. Se x=235 e y=236, então um não encaixa com o outro.
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as declarações e chamadas de funções foram implementadas corretamente de acordo com o que pede o enunciado.  
Input
Digitar dois números inteiros positivos.
Output
Mensagem informando se o número menor "encaixa"  ou "não encaixa" com o maior.
Samples Input	Samples Output
756321
123
não encaixa
80
1980
encaixa
2020
2020
encaixa
12450
245
não encaixa
123456
456
encaixa
'''
def encaixa(a,b): # a = menor  b = maior
    if a == b:
        return 'encaixa'
    
    if (len(a) == len(b)) and (a != b):
        return 'não encaixa'
    
    if len(a) > len(b):
        z = b
        b = a
        a = z

    z = b[-len(a):]
    if a == z:
        return 'encaixa'
    
    else:
        return 'não encaixa'
a = input()
b = input()
print(encaixa(a,b))