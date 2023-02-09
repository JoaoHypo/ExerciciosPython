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

options = ['A','B','C','D'] #Criando as opções
estacionados = dict() #Dicionário do estacionamento
historico = dict() #Dicionário dos carros que sairam
tarifa = 0.08 #Valor tarifa por minuto
saldo = 0 #Saldo do estacionamento

#Abrindo loop do programa
while True:
    #Printando o visual do menu
    print('ESTACIONAMENTO'.center(80,'-'))
    print('(a) Entrada de Carro: ')
    print('(b) Saída de Carro: ')
    print('(c) Listar Carros: ')
    print('(d) Fechar Estacionamento: ')
    print('(e) Terminar Programa: ')

    #Transformando em caixa alta para facilitar verificação, logo vai aceitar em caixa baixa e alta
    operacao = input('Digite a operação: ').upper()

    #Opção que finaliza o programa
    if operacao == 'E':
        print('ENCERRANDO O PROGRAMA...')
        break

    #Checando se a opção existe no menu
    if operacao not in options:
        print('\nOpção inválida, tente novamente.\n')
        continue
    
    #Criando opção (a):
    if operacao == 'A':
        print('Entrada de carro'.center(80,'-'))
        while True:
            placacarro = input('Digite a placa do carro: ')
            if placacarro in estacionados.keys(): #Checa se o carro ja está no estacionamento
                print('Carro já cadastrado, digite outra placa')
                continue

            horatxt = input('Digite a hora(HH:MM): ') #Variavel hora em formato texto/str
            hora = horatxt.split(':') #Variavel hora em formato splitado a ser convertido
            hora = (int(hora[0])*60) + int(hora[1]) #Convertendo para minutos
            estacionados[placacarro] = [horatxt,hora] #Criando o par placa - lista[horatexto,hora entrada em min]

            print(f'PLACA\tHORA ENTRADA\n{placacarro}\t{horatxt}')
            
            break

    #Criando opção (b):
    elif operacao == 'B':
        print('Saída de carro'.center(80,'-'))
        while True:
            placacarro = input('Digite a placa do carro: ')

            if placacarro in historico.keys(): #Conferindo caso o carro já tenha saido do estacionamento
                 print('Este carro já saiu do estacionamento')
                 continue
            elif placacarro not in estacionados.keys(): #Conferindo se o carro está no estacionamento
                print('Carro não encontrado, digite a placa correta')
                continue

            horatxt = input('Digite a hora(HH:MM): ') # Hora da saida 
            hora = horatxt.split(':') #Preparando para conversão de minutos
            hora = (int(hora[0]))*60 + int(hora[1]) # Convertendo para minutos
            min = (hora - estacionados[placacarro][1]) # Subtraindo saida - entrada (tempo estacionado)
            
            print(f'PLACA: {placacarro}')
            print(f'ENTRADA: {estacionados[placacarro][0]} - SAIDA: {horatxt} = {min} minutos')
            print(f'TOTAL A PAGAR: R$ {min*tarifa:.2f}')

            #Adicionando ao histório que o carro saiu, seu [ horario de entrada,saida,tempo estacionado ]
            historico[placacarro] = [estacionados[placacarro][0], horatxt, min] 
            saldo =  saldo + min*tarifa #Atualizando o saldo com o valor pago pelo carro que acaba de sair
            estacionados.pop(placacarro) #Removendo a placa do banco de dados de estacionados
            break

    #Criando opção (c):
    elif operacao == 'C':
        print(' Listar carros'.center(80,'-'))

        #Printa os carros no estacionamento, acessando os items, chaves e valores do dicionário
        print('PLACA\tHORA ENTRADA')
        for k,v in estacionados.items():  #k de keys e v de values
            print(f'{k}\t{v[0]}')

    #Criando opção (d):
    elif operacao == 'D':
        print('Fechar estacionamento'.center(80,'-'))
        if len(estacionados) > 0: #Checando se ainda há carros no estacionamento
            print('Não posso fechar, pois ainda tem carros no estacionamento')
        else:
            print('Finalizando a operação do estacionamento')
            print(f'Foram arrecadados R${saldo:.2f}') #Printando o Saldo
            
            mediamin = 0 #Pelo diconário do histórico, no terceiro item da lista que é o valor do dict.
            for val in historico.values():
                mediamin = mediamin + val[2] 

            #Devolvendo a média dividindo pelo comprimento do dict, ou seja, numero de carros que entraram e sairam
            print(f'Os clientes ficaram em média {mediamin/len(historico):.2f} minutos')
