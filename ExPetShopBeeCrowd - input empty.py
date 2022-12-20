"""
Uma Pet Shop deseja armazenar seus serviços e produtos em um programa, de acordo com a tabela abaixo. 
Quando um cliente solicitar por um serviço ou produto, o programa deverá ler o nome do cliente, nome 
do seu pet, tipo de animal (“Gato” ou “Cachorro”) e o código do serviço/produto solicitado. Caso o 
código selecionado seja de uma ração, o programa deverá perguntar, ainda, a quantidade desejada.
 Durante a leitura de informações, o programa deverá perguntar se o cliente deseja adicionar mais 
 algum serviço ou não, repetindo a execução. Serviços podem ser contratados por antecedência (não deve 
 haver controle de compra duplicada). Ao final, deverá ser fornecido um extrato completo com os dados 
 de identificação lidos e com o valor total a ser pago.

 Input

A entrada consiste no nome do cliente, seguido do nome e tipo (Cachorro ou Gato) do animal de estimação. 
Após as informações iniciais, segue uma sequência de códigos de serviços/produtos (com a quantidade desejada 
quando necessário) e indicações se há mais serviços/produtos a serem cadastrados (S - Sim, N - Não).

Output

A saída do programa deve apresentar um extrato de serviço contendo o nome do cliente, o nome do animal de 
estimação, o tipo do animal de estimação e o valor total a ser pago pelo cliente.

Samples Input	Samples Output
Bob
Bob
Gato
101
S
102
S
103
N

- Extrato do Serviço -
Cliente: Bob
Pet: Bob
Tipo: Gato
Valor total a ser pago: R$ 85.00


Fulano de Tal
Fantasma
Cachorro
102
S
105
2
N


- Extrato do Serviço -
Cliente: Fulano de Tal
Pet: Fantasma
Tipo: Cachorro
Valor total a ser pago: R$ 278.00

"""

nc = input()

np = input()

total = 0

while True:
    tp = (input()).title()
    if tp in ["Cachorro","Gato"]:
        break

while True:

    serv = int(input())
    if serv in [101,102,103,104,105]:
        pass
    
# --------------------------------  101  ------------------------------- 

    if serv == 101:
        if tp == "Gato":
            total = total + 25
        else:
            total = total + 38

        rep = (input()).upper()
        
        if rep in ["S","N"]:
            if rep == "S":
                continue
            elif rep == "N":
                break

# --------------------------------  102  ------------------------------- 

    elif serv == 102:
        if tp == "Gato":
            total = total + 15
        else:
            total = total + 28

        rep = (input()).upper()
        
        if rep in ["S","N"]:
            if rep == "S":
                continue
            elif rep == "N":
                break

# --------------------------------  103  ------------------------------- 
    elif serv == 103:
        if tp == "Gato":
            total = total + 45
        else:
            total = total + 55

        rep = (input()).upper()
        
        if rep in ["S","N"]:
            if rep == "S":
                continue
            elif rep == "N":
                break

# --------------------------------  104  ------------------------------- 

    elif serv == 104:
        qntrac = int(input())
        if tp == "Gato":
            total = total + 35*qntrac
        else:
            total = total + 55*qntrac

        rep = (input()).upper()
        
        if rep in ["S","N"]:
            if rep == "S":
                continue
            elif rep == "N":
                break

# --------------------------------  105  ------------------------------- 

    elif serv == 105:
        qntrac = int(input())
        if tp == "Gato":
            total = total + 85*qntrac
        else:
            total = total + 125*qntrac

        rep = (input()).upper()
        
        if rep in ["S","N"]:
            if rep == "S":
                continue
            elif rep == "N":
                break

print("- Extrato do Serviço -")
print(f"Cliente: {nc}")
print(f"Pet: {np}")
print(f"Tipo: {tp}")
print(f"Valor total a ser pago: R$ {total}.00")
