#Decaimento partícula

massaInicial = float(input()) #Input valor massa, float, pode ser quebrado.
MeiaVida = int(input()) #Input tempo em segundos meia vida, int
tempo = input().split(' ')

#Checamos se possui massa maior que 1g
if massaInicial > 1:

    #Aqui defimos por praticindade uma função pra converter os valores para minutos
    #para trabalhar em 1 unidade soment
    #Podem implementar manualmente sem função
    def converter_segundos(valor, unidade):
        if unidade == "h":
            return valor * 3600
        elif unidade == "min":
            return valor * 60

    #Como do terceiro input o terceiro valor ja é em segundos, vamos converter apenas 
    #o primeiro e o segundo e somar
    tempoSecs = 0

    tempoSecs = converter_segundos(int(tempo[0]),'h') #Somando a hora, primeiro termo a lista tempo, índice 0

    tempoSecs = tempoSecs + converter_segundos(int(tempo[1]),'min') #Somando os minutos, segundo termo a lista tempo, índice 1

    tempoSecs = tempoSecs + int(tempo[2]) #Somando o ultimo termo de tempo, que ja está em segundos


    #Como vamos usar a massaInicial no outro calculo, vamos criar uma copia dela
    MassaTempoFixo = massaInicial

    #Agora que temos o tempo do primeiro output, precisamos saber quantos ''tempos de decaimento'' 
    #cabem dentro desse tempo encontrado, sendo assim vamos usar divisao absoluta que ignora a sobra (//)
    for i in range(tempoSecs//MeiaVida):
        MassaTempoFixo = MassaTempoFixo/2

    #Printamos utilizando f'string com os índices do input 3, o tempo em pedaços da lista
    print(f'Massa do elemento depois de {tempo[0]}:{tempo[1]}:{tempo[2]} [g]: {MassaTempoFixo}')

    #--------------------- Agora vamos resolver o segundo output --------------------------------

    #A condição é a massa ser igual ou menor que 1, assim ela se torna indetectável
    #Comos antes nao mexemos na variavel massa inicial, agora por praticidaded manipilar por ela mesma

    #Nesta ultima etapa preciamos lidar com o resultado final em segundos, e converter para h:min:sec
    #Fizemos algo próximo nas primeiras tarefas, vou implementar como uma função a ser chamda

    def converter_secs(segundos):
        h = segundos // 3600
        min = (segundos % 3600) // 60
        restoSecs = segundos % 60
        return [h, min, restoSecs] #devolve a lista, podem implementar manualmente, sem função

    #Vamos criar um contador dos segundos para cada divisão de meia vida
    contadorAteSumir = 1

    #Loop ate sumir
    while massaInicial > 1:

        #Contando quantas 'meias vidas' foram aplicadas até sumir 
        contadorAteSumir = contadorAteSumir + 1

        #Dividindo a massa até sumir
        massaInicial = massaInicial/2

    #Multiplicamos as vezes que ele decaiu pelo tempo de decaimento e obemos a lista com hora,min,sec
    TempoFinal = converter_secs(contadorAteSumir*MeiaVida)
    
    #Printando com f'string, indce 0 é referente as horas, 1 aos minutos e 2 ao segundos restantes
    print(f'Tempo para elemento nao ser detectado: {TempoFinal[0]}:{str(TempoFinal[1]).rjust(2, "0")}:{str(TempoFinal[2]).rjust(2, "0")}')
                                                # .rjust(2, "0") é para forçar a ter 2 casas no print e completar a esquerda com 0
else:
    print('Massa do elemento nao detectada')
    print('Tempo para elemento nao ser detectado: 0:00:00')
