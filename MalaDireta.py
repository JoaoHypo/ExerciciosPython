destinos = int(input())
tabela = dict()
while len(tabela) != destinos:
    destino = input()
    envio = input()
    tabela[destino] = envio
pedidos = int(input())
contador = 0
while contador != pedidos:
    cliente = input()
    destino = input()
    print(f'{cliente} --> {tabela[destino]}')
    contador+=1