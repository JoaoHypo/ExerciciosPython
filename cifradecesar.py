'''
Cifra de Cesar

Uma Cifra de César é uma técnica de criptografia utilizada pelo imperador Júlio César para se comunicar com seus generais. Trata-se de uma técnica muito simples em que cada letra do texto é substituída por uma letra com um número fixo de posições abaixo do alfabeto.
Por exemplo, em uma cifra com um deslocamento de 3 letras, a letra A seria substituída por D, B por E e assim por diante. Quando o deslocamento ultrapassa o final do alfabeto, volta-se ao começo. Por exemplo, para o mesmo deslocamento de 3, a letra Z seria substituída por C, Y por B, e assim por diante.
Escreva uma função que é um decodificador / codificador para implementar a Cifra de César para uma palavra qualquer. Sua função deve receber três argumentos: uma palavra (str) para codificar ou decodificar, um deslocamento (int) desejado e um argumento opcional indicando se deve ser feita uma codificação ou decodificação (bool). Esse último argumento, por padrão, deve ser configurado para codificação.
Seu programa principal deverá ler o valor de deslocamento e ler duas strings opcionais, uma a ser decodificada e outra a ser codificada. Seu programa deve chamar a função duas vezes e receber os retornos dos resultados e apresentá-los na tela. 
Atenção: neste problema, mesmo que as saídas sejam todas apresentadas de forma correta e aceitas pelo Beecrowd, o professor vai avaliar se as declarações e chamadas de funções foram implementadas corretamente de acordo com o que pede o enunciado.
Input
Na primeira linha, a string de entrada (sempre minúscula) para ser codificada. Opcional.
Na segunda linha, a string de entrada (sempre minúscula) para ser decodificada. Opcional.
O valor do deslocamento.
Output
Os valores codificados e/ou decodificados para as strings informadas.
Samples Input	Samples Output
palavra

6
Saída codificada: vgrgbxg
teste
uftuf
1
Saída codificada: uftuf
Saída decodificada: teste
ikygx
wczlu
150
Saída codificada: cesar
Saída decodificada: cifra

teste
6
Saída decodificada: nymny
'''
def cifra_de_cesar(palavra, deslocamento, decodificar=False):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho_alfabeto = len(alfabeto)
    palavra_codificada = ''
    if decodificar:
        deslocamento = -deslocamento
    for letra in palavra:
        if letra not in alfabeto:
            palavra_codificada += letra
        else:
            indice_letra = alfabeto.index(letra)
            indice_letra_deslocada = (indice_letra + deslocamento) % tamanho_alfabeto
            palavra_codificada += alfabeto[indice_letra_deslocada]
    return palavra_codificada

palavra_codificada = input().strip()
palavra_decodificada = input().strip()
deslocamento = int(input())

if palavra_codificada:
    print("Saída codificada:", cifra_de_cesar(palavra_codificada, deslocamento))

if palavra_decodificada:
    print("Saída decodificada:", cifra_de_cesar(palavra_decodificada, deslocamento, decodificar=True))
