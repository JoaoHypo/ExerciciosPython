'''
Círculo circunscrito em um retângulo
Faça um programa que contenha uma função que receba como argumentos o valor da base e da altura de um retângulo. A função deverá retornar o raio, a circunferência e a área do círculo que circunscreve as dimensões informadas do retângulo (como apresentado na figura abaixo). Após isto, o programa principal deve mostrar na tela os valores retornados pela função. Utilize o módulo math para acessar a função math.sqrt e a constante math.pi. Também, as equações abaixo podem ser utilizadas para obter os valores requisitados.



Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as declarações e chamadas de funções foram implementadas corretamente de acordo com o que pede o enunciado.
Input
Entrada em duas linhas:
Na primeira linha, valor da base do retângulo. Um número real (float).
Na segunda linha, valor da altura do retângulo. Um número real (float).
Output
A saída deve apresentar o valor do raio do círculo circunscrito, a área e a circunferência (todos com duas casas decimais) de acordo com o exemplos.
Samples Input	Samples Output
20
1
Raio: 10.01
Área: 314.94
Circunferência: 62.91
10
10
Raio: 7.07
Área: 157.08
Circunferência: 44.43
15
10
Raio: 9.01
Área: 255.25
Circunferência: 56.64
'''

import math

def circunscrito_retangulo(base, altura):
    diagonal = math.sqrt(base**2 + altura**2)
    raio = diagonal/2
    area = math.pi * raio**2
    circunferencia = 2 * math.pi * raio
    return raio, area, circunferencia

base = float(input())
altura = float(input())

raio, area, circunferencia = circunscrito_retangulo(base, altura)

print(f"Raio: {raio:.2f}")
print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")
