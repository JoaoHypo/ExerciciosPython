'''
Histórico uso apps

Faça um programa, utilizando dicionários, que armazena o histórico de uso de aplicativos de
 um smartphone. O programa lerá alternadamente o nome do aplicativo e o tempo de utilização 
 do mesmo. Caso seja inserido um nome já existente no histórico, o tempo de utilização é somado 
 com o tempo de utilização já existente. O programa termina quando ler uma linha em branco. 
 Após isso, o programa exibe o ranking de aplicativos na ordem de utilização
 (do mais usado para o menos).
Input
O nome do aplicativo em uma linha, seguido do respectivo tempo de utilização na próxima linha. 
O fim da entrada será indicado por uma linha vazia, em branco.
Output
A relação de aplicativos e o tempo total de uso de cada um em ordem decrescente de uso. 
O seu programa deve usar uma tabulação para separar a palavra Aplicativo da frase Tempo 
de Utilização. Da mesma forma, o seu programa deve separar o nome do aplicativo do número 
indicando o tempo de uso também por uma tabulação. Por exemplo:
print ("Aplicativo\tTempo de Utilização")
Samples Input	Samples Output
Facebook
4
Whatsapp
5
Instagram
7
Whatsapp
3

Aplicativo      Tempo de Utilização
Whatsapp        8
Instagram       7
Facebook        4
Whatsapp
6
Facebook
4
Facebook
1
Instagram
5
Whatsapp
3
Whatsapp
2
Google Maps
1
Calculadora
2
Whatsapp
3
Instagram
5

'''


aplicativos = dict()
while True:
    entrada = input()
    if entrada == '':
        break
    usos = int(input())
    aplicativos[entrada] = aplicativos.get(entrada,0) + usos

temp = (sorted([(usos,app) for app,usos in aplicativos.items()],reverse=True))

print ("Aplicativo\tTempo de Utilização")
for usos,app in temp:
    print(f"{app}\t{usos}")
