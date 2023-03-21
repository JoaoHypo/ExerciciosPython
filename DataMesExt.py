'''
Data com mês por extenso

Timelimit: 2
Faça um programa com duas funções: A primeira recebe como argumento uma data (string) no formato DD/MM/AAAA e retorna a mesma data (string) no formato DD de M (por extenso) de AAAA. A segunda recebe três valores inteiros, dia, mês e ano, e verifica se estes formam uma data válida (dia entre 1 e 31, de acordo com o mês informado, mês entre 1 e 12 e ano maior que 0), retornando o valor booleano (True ou False) apropriado. A primeira função deve chamar a segunda para checar a validade da data, retornando a string “Data inválida” caso não possa ser transformada no formato por extenso ou o string da data convertida no formato por extenso caso contrário. No programa principal o usuário deve informar uma data a ser colocada por extenso, a função que converte a data deve ser chamada e o resultado retornado pela função deve ser impresso na tela pelo programa principal.  
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as declarações e chamadas de funções foram implementadas corretamente de acordo com o que pede o enunciado.
Detalhe: Ao verificar se a data é válida ignore anos bissextos.
Input
Digitar uma data no formato DD/MM/AAAA.
Output
Data por extenso ou mensagem de erro (Data inválida).
Samples Input	Samples Output
15/04/0900
15 de abril de 0900
12/10/1492
12 de outubro de 1492
01/99/2020
Data inválida
13/09/1970
13 de setembro de 1970
31/04/2022
Data inválida
01/01/0000
Data inválida
'''

def data_extenso(data):
    dia, mes, ano = data.split('/')
    if verifica_data(int(dia), int(mes), int(ano)):
        mes_extenso = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 
                       7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
        return f'{dia} de {mes_extenso[int(mes)]} de {ano}'
    else:
        return 'Data inválida'

def verifica_data(dia, mes, ano):
    if mes < 1 or mes > 12 or dia < 1:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2 and dia > 28:
        return False
    if mes == 2 and dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
        return False
    if dia > 31:
        return False
    return True

data = input()
print(data_extenso(data))
