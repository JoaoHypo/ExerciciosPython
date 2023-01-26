'''
Sorteio
Todo: Add text
'''

import random
pontos1 = []
pontos2 = []
while True:
    jogador1 = []
    jogador2 = []
    sorteados = []
    while len(jogador2) < 5:
        numero = int(input())
        if numero == 0: break   
        if 0 < numero <= 20:
            if len(jogador1) < 5:
                jogador1.append(numero)
            elif len(jogador2) < 5:
                jogador2.append(numero)             
                  
    if numero == 0: break   
    random.seed(1024) #Random Seed tem q ser declarado a cada loop, pq sim kkkk
    while len(sorteados) < 5:
        sorteado = random.randint(1, 20)
        if sorteado not in sorteados:            
            sorteados.append(sorteado)
    
    ponto1Rodada = (len(set(jogador1).intersection(sorteados)) * 10)
    pontos1.append(ponto1Rodada)

    ponto2Rodada = (len(set(jogador2).intersection(sorteados)) * 10)        
    pontos2.append(ponto2Rodada)    
    
    print(f"JOGADOR 1 = {ponto1Rodada}, JOGADOR 2 = {ponto2Rodada}")


if sum(pontos1) > sum(pontos2):
    print("JOGADOR 1 VENCEU!")
elif sum(pontos1) < sum(pontos2):
    print("JOGADOR 2 VENCEU!")
else:
    print("EMPATE!")