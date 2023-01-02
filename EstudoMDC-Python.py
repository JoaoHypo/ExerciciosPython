'''
O MDC de dois números é o último resto da divisão do maior número pelo menor.
Todo: Gerar JupyNotebook com estes dados posteriormente!
'''
# Calculando com loop de função lidando matematicamente com a ordem do maior e menor
# Abordagem + matmática
def mdc(a, b):

    if b == 0:
        return a
        
    else:
        print(a,b)  # print teste

        print(a % b) #O Loop força b sempre ser o menor numero de resto
                     #Logo, num cenário de rest/o 0, o outro valor é o MDC
                     #E caso B seja maior no primeiro loop os valores são invertidos!
                     # Porque o primeiro resto vai ser justamente o termo "a" inteiro!

        return mdc(b, a % b) # Aqui descobri que return so realmente devolve
                             # Algo na tela, se for return com print, que 
                             # também não é ideal, e também que é possivel
                             # Fazer Loops dentro de uma função, mesmo sem While
                             # Ou for loops

resultado = mdc(9, 27) 
resultado2 = mdc(27,9)
print("resultado 1=",resultado,"\nresultado 2=",resultado2)

# Abordagem menos matemática + programação:

def mdc2(a,b):
    lista = [a,b]
    lista.sort()
    calc = lista[1]%lista[0]
    if calc == 0:   #sem este bloco if em divisoes exatas temos o resultado errado de 0 como MDC
        return lista[0]  # retorna o menor numero quando resto é 0
                         # !!! Divisão inteira.
    else: 
        return calc

resultado3 = mdc2(27,9)
print("resultado 3=",resultado3)

# Testando com numeros de resto 0, entendnedo que a primeira função não tem falhas 
# Não precisa de correções com if's e por isso provavelmente roda mais rápidamente
# Além de armazenar o ultimo menor divisor pela logica de inversão dos termos.
