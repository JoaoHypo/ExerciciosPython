'''
Faça um programa que contenha uma classe IntSet. No método de inicialização __init__ desta classe, deve ser inicializado um atributo vals do tipo lista. Esta classe também deve conter outros dois métodos. O primeiro método deve receber como argumento um número inteiro e deve adicionar este valor na lista vals somente se o valor ainda não está presente nesta lista. Já o segundo método deve retornar uma string que representa os valores contidos em vals no formato {v1, v2, v3, ...}. No programa principal, deve ser feita a instanciação de um único objeto da classe IntSet, juntamente com um laço para a inserção dos valores. O laço deve se repetir até que a string “sair” seja digitada, quando deverá ser exibido o conjunto de inteiros presentes na classe IntSet e então encerrar o programa.
Atenção: Deve-se obrigatoriamente utilizar noções de Programação Orientada a Objetos para resolver esse exercício.Para obter a nota total, é necessário implementar todo o código conforme o solicitado no enunciado. Soluções que não o façam perderão nota, mesmo se o Beecrowd julgar o código como Accepted.    
Dica: utilize a função auxiliar isNumber(s) para verificar se uma determinada string "s" é um número inteiro.
def isNumber(s):
    try:
        int(s)
    except Exception:
        return False
    else:
        return True
Entrada
A entrada é composta por múltiplos números inteiros, um em cada linha. A última linha apresenta a palavra sair que sinaliza o final da entrada de dados.
Saída
Na primeira linha da saída deve-se apresentar a mensagem - Conjunto de inteiros:
Na segunda linha, devem ser impressos os valores armazenados na classe IntSet, seguindo a formatação: {v1, v2, v3, ..., vn} onde, v1, v2, v3, .. , vn são números diferentes entre si e aparecem na ordem em que foram informados na entrada.
Samples Input	Samples Output
1
3
5
5
5
-2
1
sair
Conjunto de inteiros:
{1, 3, 5, -2}
9
-8
3
1
6
-5
8
9
6
7
3
6
8
2
-9
sair
Conjunto de inteiros:
{9, -8, 3, 1, 6, -5, 8, 7, 2, -9}

'''

def isNumber(s):
    try:
        int(s)
    except Exception:
        return False
    else:
        return True

class IntSet:
    def __init__(self):
        self.vals = []

    def add(self, value):
        if value not in self.vals:
            self.vals.append(value)

    def __str__(self):
        if len(self.vals) == 0:
            return "{}"
        else:
            result = "{"
            for i in range(len(self.vals)-1):
                result += str(self.vals[i]) + ", "
            result += str(self.vals[-1]) + "}"
            return result

intSet = IntSet()
print("Conjunto de inteiros:")
while True:
    value = input().strip()
    if value == "sair":
        break
    if isNumber(value):
        intSet.add(int(value))

print(intSet)
