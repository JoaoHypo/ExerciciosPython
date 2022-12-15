#EP04-B - Óvos de Páscoa

''' Uma indústria de ovos de Páscoa fornece três tipos diferentes de ovos de chocolate: Simples, Recheado e Com surpresa. Com a intenção de fazer uma Páscoa feliz para um maior número de clientes possível, a quantidade de ovos por pedido é limitada. Abaixo está o detalhamento dos produtos e limites:
        ● Simples (A): com valor unitário de R$12.00, limite por pedido 50.
        ● Recheado (B): com valor unitário de R$ 15.50, limite por pedido 30.
        ● Com surpresa (C): com valor unitário de R$21.30, limite por pedido 20.
Seu programa deve ler os dados de um pedido (um tipo de ovo e uma quantidade) e informar:
       ● O produto solicitado (nome do tipo de ovo), controlando que o tipo informado seja válido. Apresentar a mensagem "Produto inválido" caso o tipo de ovo não exista;
       ● O número de unidades vendidas (se o limite do tipo solicitado for ultrapassado, incluir no pedido apenas a quantidade limite e incluir a mensagem "Limite excedido");
       ● O total a ser pago, em reais. 
Caso a quantidade de ovos digitada pelo usuário não seja do tipo inteiro e positivo o programa deverá mostrar a mensagem "Quantidade inválida" e não realizar o pedido.
Input
Entrar com o tipo de ovo (A, B ou C), quantidade (int).
Output
Nome do produto, quantidade adquirida e valor total do pedido. Formate o valor total do pedido na saída com duas casas decimais.  
Samples Input	Samples Output
A
0.5
Quantidade inválida
X
2
Produto inválido
C
1
Pedido: 1 ovos do tipo Com surpresa (C)
Valor Total: R$ 21.30
B
100
Pedido: 30 ovos do tipo Recheado (B)
Valor Total: R$ 465.00
Limite excedido
A
12
Pedido: 12 ovos do tipo Simples (A)
Valor Total: R$ 144.00

'''

tipo = input()
qnt = input()
limit = False

if tipo not in ['A','B','C']:
        print("Produto inválido")

try:

    if int(qnt) < 1:
        print("Quantidade inválida")

    if tipo == "A":
        if int(qnt) > 50:
            qnt = 50
            limit = True
        else:
            qnt = int(qnt) 

    elif tipo == "B":
        if int(qnt) > 30:
            qnt = 30
            limit = True 
        else:
            qnt = int(qnt) 

    elif tipo == "C":
        if int(qnt) > 20:
            qnt = 20
            limit = True
        else:
            qnt = int(qnt)  
   
    if tipo == "A":
        print(f'Pedido: {qnt} ovos do tipo Simples (A)')
        print(f'Valor Total: R$ {(12.00*qnt):.2f}')
        
    elif tipo == "B":
        print(f'Pedido: {qnt} ovos do tipo Recheado (B)')
        print(f'Valor Total: R$ {(15.50*qnt):.2f}') 

    elif tipo == "C":
        print(f'Pedido: {qnt} ovos do tipo Com surpresa (C)')
        print(f'Valor Total: R$ {(21.30*qnt):.2f}')

    if limit == True:
        print("Limite excedido")

except:
    print("Quantidade inválida")
