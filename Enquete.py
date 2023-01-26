'''
Enquete
Uma emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faça um programa onde o usuário digitará um número, entre 1 e 24, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo e aguardar o próximo número. Após o final da votação, o programa deverá exibir o total de votos computados, o número e porcentagem dos votos de todos os jogadores que receberam votos, e o jogador mais votado.
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as estruturas de dados (listas) foram implementadas corretamente.        
Input
A entrada é formada por números inteiros positivos pertencentes ao intervalo fechado de 1 a 24. Esses números representam os números das camisas dos jogadores.
Números fora desse intervalo devem ser ignorados pelo seu programa.
O número 0 (zero) sinaliza ao programa que a execução deve ser finalizada.
Output
A saída do programa deve apresentar: o total de votos computados, o resultado da votação para cada jogador com quantidade de votos diferente de zero e o jogador mais votado, obedecendo à formatação a seguir.
Na primeira linha deve-se imprimir o total de votos computados, ou seja, os votos pertencentes ao intervalo de 1 a 24. A apresentação da mensagem deve obedecer a seguinte formatação:
TOTAL DE VOTOS = A, onde a letra A deve ser substituída pelo total de votos válidos.
A partir da segunda linha deve-se imprimir o resultado da votação para cada jogador no seguinte formato:
JOGADOR = B, VOTOS = C, PERCENTUAL = D%, onde B, C e D devem ser substituídas por, respectivamente: número da camisa do jogador, total de votos recebido por ele, porcentagem de votos recebida com relação ao total (número inteiro, ou seja, sem vírgula).
Na última linha deve-se apresentar a mensagem:
MELHOR JOGADOR = E, onde E deve ser substituída pelo número da camisa do jogador mais votado.
Samples Input	Samples Output
5
5
20
20
1
1
1
0
TOTAL DE VOTOS = 7
JOGADOR = 1, VOTOS = 3, PERCENTUAL = 42%
JOGADOR = 5, VOTOS = 2, PERCENTUAL = 28%
JOGADOR = 20, VOTOS = 2, PERCENTUAL = 28%
MELHOR JOGADOR = 1
5
3
1
9
5
7
24
24
-5
8
22
50
24
6
66
0
TOTAL DE VOTOS = 12
JOGADOR = 1, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 3, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 5, VOTOS = 2, PERCENTUAL = 16%
JOGADOR = 6, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 7, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 8, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 9, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 22, VOTOS = 1, PERCENTUAL = 8%
JOGADOR = 24, VOTOS = 3, PERCENTUAL = 25%
MELHOR JOGADOR = 24
9
7
9
25
8
0
TOTAL DE VOTOS = 4
JOGADOR = 7, VOTOS = 1, PERCENTUAL = 25%
JOGADOR = 8, VOTOS = 1, PERCENTUAL = 25%
JOGADOR = 9, VOTOS = 2, PERCENTUAL = 50%
MELHOR JOGADOR = 9

'''
voto = None
votos = []
contadorVotos = 0
while voto != 0:
    voto = int(input())
    if voto < 1 or voto > 24:
        pass
    else:
        adiconado = False
        if contadorVotos == 0:
            votos.append([voto,0])
        contadorVotos += 1
        for dados in votos:
            if voto == dados[0]:
                dados[1] = dados[1] + 1
                adiconado = True
                break
        if adiconado == False:
            votos.append([voto,1])
print(f"TOTAL DE VOTOS = {contadorVotos}")

maior = 0
indexMaior = 0
votos.sort()
for index,dados in enumerate(votos):
    if dados[1] > maior:
        maior = dados[1]
        indexMaior = index
    print(f'JOGADOR = {dados[0]}, VOTOS = {dados[1]}, PERCENTUAL = {int((100*dados[1])/contadorVotos)}%')
print(f'MELHOR JOGADOR = {votos[indexMaior][0]}')
