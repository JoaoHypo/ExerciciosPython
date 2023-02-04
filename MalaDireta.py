'''
Mala Direta
Os Correios contrataram você para desenvolver um novo sistema de Mala Direta, no qual dado 
o endereço de uma pessoa, o sistema indique o método de envio que deve ser usado para enviar 
a correspondência a essa pessoa.
O programa deverá ler um conjunto M de destinos e o respectivo método de envio de correspondência
 para que a mesma chegue a esse destino, e outro conjunto N de pessoas e seus respectivos
  endereços, que mapeiam para um dos destinos do conjunto M. O seu programa deverá gerar
   como saída uma relação com o nome da pessoa e o método que deve ser usado para enviar
    uma correspondência a essa pessoa.
Atenção: neste exercício é obrigatório o uso de dicionários. Mesmo que o resultado da 
saída do programa seja aceito pelo Beecrowd, o professor irá avaliar o uso dessas 
estruturas adequadamente na solução.  
Entrada
A entrada será iniciada por um número M, indicando o tamanho do conjunto de destinos.
 A seguir, serão informados M destinos e os respectivos métodos de envio, sendo o nome 
 do destino em uma linha, e o método de envio na próxima linha.
A seguir, será informado um número N, indicando o tamanho da lista de pessoas. A seguir 
serão informadas N pessoas e os respectivos endereços, sendo o nome da pessoa em uma linha
 e o endereço (destino) na próxima linha.
Saída
O seu programa deverá gerar como saída a relação de pessoas com o respectivo método de envio
 que deve ser usado para enviar a correspondência a essa pessoa. O nome da pessoa deverá ser 
 separado do método de transporte por uma seta representada por --> (sinal de menos, sinal de
  menos, sinal de maior que).

Samples Input	Samples Output
4
Winterfell
Carroça
Iron Islands
Barco
Kings Landing
Dragão
Castle Black
Corvo
5
Jon Snow
Castle Black
Cersei Lannister
Kings Landing
Theon Greyjoy
Iron Islands
Arya Stark
Winterfell
Daenerys Targaryen
Kings Landing
Jon Snow --> Corvo
Cersei Lannister --> Dragão
Theon Greyjoy --> Barco
Arya Stark --> Carroça
Daenerys Targaryen --> Dragão
3
Itaituba
Transporte Aéreo
Porto Alegre
Transporte Rodoviário
São Paulo
Transporte Marítimo
4
Ana Paula
Itaituba
Juliano Wickboldt
Porto Alegre
Maria Souza
São Paulo
Weverton Cordeiro
Itaituba
'''

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