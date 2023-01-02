#Collectable Cards com input tipo: 12 8
#Necessitando de umas alterações nos inputs
N = int(input())

testctrl = 0

result = []

while testctrl < N:

    cartas = input().split()
    lista = [int(i) for i in cartas]
    lista.sort()
    calc = lista[1]%lista[0]
    if calc==0:
        print(lista[0],end='')
    else:    
        print(calc,end='')
    testctrl += 1
