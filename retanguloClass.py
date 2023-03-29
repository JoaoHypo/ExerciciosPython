'''
Faça um programa que contenha uma classe Retangulo. No método de inicialização __init__ desta classe, devem ser passados dois argumentos inteiros: base e altura. Esta classe também deve conter outros três métodos. O primeiro método deve retornar uma string que representa as dimensões do retângulo no formato (base, altura). O segundo método deve retornar a área do retângulo com base nas dimensões informadas. Já o terceiro método deve retornar o perímetro do retângulo com base nas dimensões informadas. No programa principal, faça um laço onde em cada passo um objeto da classe Retângulo é instanciado. Após um retângulo ser instanciado, mostre os valores correspondentes às suas dimensões, a sua área e seu perímetro.
Atenção: Deve-se obrigatoriamente utilizar noções de Programação Orientada a Objetos para resolver esse exercício.Para obter a nota total, é necessário implementar todo o código conforme o solicitado no enunciado. Soluções que não o façam perderão nota, mesmo se o Beecrowd julgar o código como Accepted.  
Entrada
A primeira linha da entrada apresenta um número inteiro N que representa a quantidade de linhas de entrada que seguem.
As demais linhas são formadas por um par de número inteiros separados por um espaço: BASE ALTURA
Saída
Para cada linha da entrada devem ser geradas 3 linhas de saída.
Na primeira linha serão informadas as dimensões do retângulo no formato - Dimensões: (BASE, ALTURA)
Na segunda linha deve ser impressa a área do retângulo no formato - Área = AREA
De forma análoga, na terceira linha deve-se imprimir o perímetro do retângulo - Perímetro = PERIMETRO
Samples Input	Samples Output
2
59 35
698 581
Dimensões: (59, 35)
Área = 2065
Perímetro = 188
Dimensões: (698, 581)
Área = 405538
Perímetro = 2558
4
4 6
8 5
9 3
1 7
Dimensões: (4, 6)
Área = 24
Perímetro = 20
Dimensões: (8, 5)
Área = 40
Perímetro = 26
Dimensões: (9, 3)
Área = 27
Perímetro = 24
Dimensões: (1, 7)
Área = 7
Perímetro = 16

'''


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def dimensoes(self):
        return f"Dimensões: ({self.base}, {self.altura})"

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Lê o número de retângulos a serem criados
n = int(input())

# Instancia os n retângulos e exibe as informações de cada um
for i in range(n):
    base, altura = map(int, input().split())
    retangulo = Retangulo(base, altura)
    print(retangulo.dimensoes())
    print(f"Área = {retangulo.area()}")
    print(f"Perímetro = {retangulo.perimetro()}")