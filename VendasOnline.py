'''
Vendas online
Uma empresa contratou você para desenvolver um programa para gerenciar vendas online. Este programa pode receber 4 requisições:
          1 -  Cadastro: um produto a ser cadastrado contem um código de identificação (ID), um nome, uma quantidade e um valor. O código de cada produto será único
          2 -  Venda:  uma venda contém o ID do produto e uma quantidade. Para uma venda ser efetuada, o código do produto deve existir e deve haver quantidade suficiente em estoque. Caso isso não ocorra, a venda é ignorada sem nenhuma mensagem de aviso. Quando uma venda é efetuada, a quantidade requisitada é descontada da quantidade em estoque e o valor total da compra é exibido.  Caso a quantidade de um produto chegue a zero, este deve ser removido do cadastro;
          3 -  Exibir:  exibe todos os produtos disponíveis para venda, contendo o ID, nome, quantidade e valor;
          0 -  Finalizar: termina o programa e exibir o valor total de produtos vendidos;
Input
A entrada é formada pelo número da requisição e informações de necessárias para a sua execução.
Os números das requisições são os seguintes inteiros: 1 - para Cadastro, 2 - para Venda, 3 - para Exibir ou 0 - para Finalizar.
Quando necessário, os dados da operação são apresentados na linha após o número da requisição. Os itens dessa linha são separados por uma vírgula seguida de um espaço ", ".
Por exemplo: Para a operação de cadastro são informados os seguintes itens: 
ID (número inteiro), nome (string), quantidade (número inteiro) e valor (número real)
Output
A saída é formada por múltiplas linhas dependentes da ordem das operações.
Para a operação 3 (Exibir) são apresentadas as informações dos produtos na seguinte formatação: ID: X, NOME: Y, QUANTIDADE: Z, VALOR: W, onde X é o código do produto, Y o nome, Z a quantidade e W o valor por unidade.
Para a operação 2 (Venda) será exibido o valor da compra com a mensagem:  VALOR DA COMPRA: R$ K, onde K representa o valor da compra realizada pelo cliente com duas casas decimais.
Na última linha da saída deve-se imprimir: TOTAL VENDIDO: R$ J, onde J é o valor acumulado das vendas com duas casas decimais.
Samples Input	Samples Output
1
100, Pizza, 5, 40.90
3
0
ID: 100, NOME: Pizza, QUANTIDADE: 5, VALOR: 40.90
TOTAL VENDIDO: R$ 0.00
1
100, Pizza, 5, 40.90
1
35, Miojo Sabor Galinha, 100, 2.20
1
18, Coca-Cola, 5, 8.49
3
2
18, 6
2
100, 5
2
57, 9
3
0
ID: 100, NOME: Pizza, QUANTIDADE: 5, VALOR: 40.90
ID: 35, NOME: Miojo Sabor Galinha, QUANTIDADE: 100, VALOR: 2.20
ID: 18, NOME: Coca-Cola, QUANTIDADE: 5, VALOR: 8.49
VALOR DA COMPRA: R$ 204.50
ID: 35, NOME: Miojo Sabor Galinha, QUANTIDADE: 100, VALOR: 2.20
ID: 18, NOME: Coca-Cola, QUANTIDADE: 5, VALOR: 8.49
TOTAL VENDIDO: R$ 204.50
1
100, Pizza, 5, 40.90
1
35, Miojo Sabor Galinha, 100, 2.20
1
18, Coca-Cola, 5, 8.49
3
2
100, 5
2
18, 5
3
0
ID: 100, NOME: Pizza, QUANTIDADE: 5, VALOR: 40.90
ID: 35, NOME: Miojo Sabor Galinha, QUANTIDADE: 100, VALOR: 2.20
ID: 18, NOME: Coca-Cola, QUANTIDADE: 5, VALOR: 8.49
VALOR DA COMPRA: R$ 204.50
VALOR DA COMPRA: R$ 42.45
ID: 35, NOME: Miojo Sabor Galinha, QUANTIDADE: 100, VALOR: 2.20
TOTAL VENDIDO: R$ 246.95
'''

controle = None
cadastro = []
total = 0

while controle != '0': 

    controle = input()

    if controle == '1':
        tl = input().split(', ')
        cadastro.append([tl[0],tl[1],tl[2],tl[3]])

    elif controle == '2':
        pedido = input().split(', ')
        for item in cadastro:
            if item[0] == pedido[0]:
                if int(item[2]) - int(pedido[-1]) >= 0:
                    item[2] = int(item[2]) - int(pedido[-1])
                    valorpedido = (float(item[-1])*int(pedido[-1]))
                    total = total + valorpedido
                    print(f'VALOR DA COMPRA: R$ {valorpedido:.2f}')

    elif controle == '3':
        for item in cadastro:
            if int(item[2]) >= 1:
                print(f'ID: {item[0]}, NOME: {item[1]}, QUANTIDADE: {item[2]}, VALOR: {item[3]}')
print(f'TOTAL VENDIDO: R$ {total:.2f}')
