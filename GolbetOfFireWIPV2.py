# pegar o menor primo
# achar a potencia máxima do problema 
# testar os pares de potencia dos 2

def IsNumPrime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_duplicates(lst):

    duplicates = []

    for element in lst:
        if lst.count(element) > 1:
            duplicates.append(element)

    return duplicates

def FireGoblet(n,p):

    primes = []

    for i in range(p):
        test = IsNumPrime(i)
        if test == False:
            continue
        else:
            primes.append(i)

    nfac = n
    factors = []
    multiplos = [1] + primes

    for i in primes:
        while nfac % i == 0:
            nfac = nfac/i
            factors.append(i)

    pot2 = []
    duplicates = find_duplicates(factors)
    for i in duplicates:
        if i not in pot2:
            pot2.append(i)
    
    for i in pot2:  
        multiplos.append(i**2)

    multi = 1
    for i in factors:

        multi = multi*i
        if multi not in multiplos:
            multiplos.append(multi)

        for j in range(len(factors)):
            multi4 = multi*factors[j]
            if multi4 not in multiplos:
                multiplos.append(multi4) 

            for j in range(len(factors)):
                multi2 = i*factors[j]
                if multi2 not in multiplos:
                    multiplos.append(multi2)

                for k in range(len(factors)):
                    multi3 = multi2*k
                    if multi3 not in multiplos:
                        multiplos.append(multi3)

    multiplos.sort()
    multiplos.remove(0)
    resposta= []
    for i in multiplos:
        if n%i != 0:
            pass
        else:
            resposta.append(i)
        
    return resposta

try:
    n1 = int(input())
    while True:
        p = int(input())
        n = n1*p
        print(FireGoblet(n,p))
except:
    pass
