'''
1. Questão Única – O Estacionamento

Um estacionamento necessita de um programa para controlar sua operação. Escreva um programa para
controlar a entrada e saída de automóveis do estacionamento, bem como a cobrança pelo tempo estacionado.
O estacionamento cobra uma tarifa fixa por minuto estacionado. Seu programa deve iniciar lendo este valor.
Após isso, um menu deve ser exibido para o usuário, contendo as seguintes operações:


(a) Entrada de Carro: Deve ser solicitado ao usuário que informe o número da placa e o horário de entrada
do carro. Em seguida esses valores devem ser salvos em um dicionário.
Não podem existir dois carros com a mesma placa no estacionamento. Caso o usuário informe um número
de placa já existente, deve ser solicitado que ele informe outro valor.
Assuma que o usuário sempre digitará um horário no formato HH:MM.
(b) Saída de Carro: Nesta opção o usuário informa a placa de um carro. (Ele deve repetir a digitação até
que seja informada uma placa de carro existente) e a hora da saída (no mesmo formato que a hora de
entrada).
Deve ser calculado o total a ser pago (número de minutos que o carro permaneceu estacionado * valor
da tarifa por minuto). Uma mensagem deve ser exibida para o usuário e essas informações devem ser
salvas.

(c) Listar Carros: Essa opção deve exibir uma relação contendo a placa e o horário de entrada dos carros que
estão no estacionamento. Note que não devem ser mostrados os carros que já sairam do estacionamento.

d) Fechar Estacionamento: Ao escolher esta opção, deve-se primeiramente verificar se ainda existem
carros no estacionamento que ainda não fizeram sua saída. Nesse caso, o sistema deve mostrar uma
mensagem informando que não é possível fechar o estacionamento.
Caso o estacionamento possa ser fechado, devem ser apresentadas duas informações: o total em dinheiro
arrecadado pelo estacionamento e a média de minutos que os carros passaram estacionados.


Informações Adicionais:

• Deve-se obrigatoriamente utilizar um dicionário para representar os dados dos carros no estacionamento.
Utilize a placa do carro como chave.
• Os dados dos carros que entraram e saíram podem ser mantidos na mesma estrutura ou em estruturas
diferentes. Cada programador pode decidir como lidar com esses dados.
• Abaixo é mostrada um exemplo de utilização desse programa. Neste exemplo o menu foi omitido para
facilitar a apresentação. As anotações em vermelho servem somente para auxiliar no entendimento do
programa.

'''

#Criando as opções
options = ['A','B','C','D']
Dados = dict()

#Abrindo loop do programa
while True:

    print('ESTACIONAMENTO'.center(80,'-'))
    print('(a) Entrada de Carro: ')
    print('(b) Saída de Carro: ')
    print('(c) Listar Carros: ')
    print('(d) Fechar Estacionamento: ')
    #Transformando em caixa alta para facilitar verificação, logo vai aceitar em caixa baixa e alta
    operacao = input('Digite a operação: ').upper()
    
    #Checando se a opção existe
    if operacao not in options:
        print('\nOpção inválida, tente novamente.\n')
        continue
    
    #Criando opção (a):
    if operacao == 'A':
        while True:
            placacarro = input('Digite a placa do carro: ')
            if placacarro in Dados.keys():
                print('Carro já cadastrado, digite outra placa')
                continue
            hora = input('Digite a hora(HH:MM): ').split(':')
            hora = int(hora[0])*60 + int(hora[1])
            Dados[placacarro] = hora
            print(Dados)
            break

    #Criando opção (b):
    elif operacao == 'B':
        pass


    #Criando opção (c):
    elif operacao == 'C':
        pass


    #Criando opção (c):
    elif operacao == 'C':
        pass
