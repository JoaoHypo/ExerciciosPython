#Collectable Cards com input tipo: 12 8
#Necessitando de umas alterações nos inputs
# Note: Funções >>>>>>>>>>> código estruturado
# return é mais conciso como resultado do que um print de um objeto

def mdc(a, b): # Abordagem matemática peca na legibilidade porém
               # Vence em todos outros aspectos técnicos do código
    if b == 0:
        return a        
    else:
        return mdc(b, a % b)

n = int(input())

for i in range(n):
    cartas = [int(i) for i in input().split()]
    print(mdc(cartas[0],cartas[1]))
