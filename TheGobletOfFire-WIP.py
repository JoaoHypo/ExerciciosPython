'''
The Goblet of Fire

One of the trials of the Triwizard Tournament will be a football match, and Chapecoense has
been training hard to face Hogwarts players. The Chapecoense Football Association
(in Portuguese: Associação Chapecoense de Futebol, or shortly ACF, or simply Chapecoense) 
is the football team of the city of Chapecó. Founded in 1973, the team nowadays plays among 
the best teams of Brazil, and it is not some freak teenagers of hat and broomstick that are 
going to frighten our brave warriors, even though we all have been shocked when the Goblet 
of Fire chose our muggle players to participate of the Triwizard Tournament. As we have 
previously mentioned, the history of the team begins in 1973 when…

We interrupt this text for the transmission of an urgent message of the Minister of Magic.

Good afternoon, muggle ladies and gentlemen! Cursed be the day in which Dolores Umbridge has 
left the prison. Now, she lives to piss me off with those Math problems. And she knows I'm not
good at these things. So, can you write a program to help me? The problem is: she says to me 
an integer N and asks me to tell how many divisors N has and to keep this N in my head. So far 
so good. I'm not that stupid and I don't need help in this part. But then she keeps saying to
me some prime numbers and, for each prime p she says, I'm supposed to multiply p by N, updating 
the value of N in my head, and, as if it were not enough, I still have to tell her how many 
divisors this new N has which are composed only by prime factors less than p. For example,
if I have kept in my head N = 630 and she says p = 5, I must update N to 3150 and say 6, 
for the only divisors of 3150 composed only by prime factors less than 5 are: 1, 2, 3, 6, 9 
and 18. But the number N grows very quickly, and I don't want to lose the game to her. Please
do something!

Input
The input consists of at least 2 and at most 105 lines. The first line consists of the single
integer N (2 ≤ N ≤ 1012). Each one of the next lines consist of a single prime number
p (2 ≤ p ≤ 107). The integers are given in the input in the order that Dolores Umbridge 
says them. The input ends in end of file.

Output
For each prime number p said by Dolores Umbridge, print a line consisting only of the answer
that the Minister of Magic was supposed to give her. As the answer can be a very large number,
print only the remainder that is left when the answer is divided by 109 + 7.


Input Samples	
630
5
7
2
3
11

Output Samples
6
18
1
3
108

------------------------------------------------

Input Samples
2
3
5
7
11

Output Samples
2
4
8
16
------------------------------------------------

Input Samples
2
2
2
2
3

Output Samples
1
1
1
5
'''


#Criando função que checa se numero é primo
def IsNumPrime(n):

    if n <= 1:
        return False

    #Checa se o numero realmente é primo, 
    #não podendo ser divisível por qualquer numero menor
    for i in range(2, n):
        if n % i == 0:
            return False
    #Do contrário, temos um primo!
    return True


#Criando a função de checagem dos dívisiveis mútiplos 
def FireGoblet(n,p):

    multiplos = []
    #Aqui armazenamos os primos
    primes = []

    #Neste Loop for vamos conferir e armazenas os primos no range de p
    #Nunca adiciona o p, como pedido no exercício justamente pq o intervalo range
    #tem o final do limite aberto [0,p), podendo ser corrigido dependendo da aplicação
    #por um range  de p+1, que se livra do primeiro termo 0, que não é primo, e 
    #adiciona o termo p, ficando com intervalo (1,p)
    for i in range(p):
        test = IsNumPrime(i)
        if test == False:
            continue
        else:
            primes.append(i)

    nfac = n
    factors = []

    #Aqui fatoramos o de n somente com os primos menores que p
    #e os adicionamos a uma lista
    for i in primes:
        while nfac % i == 0:
            nfac = nfac/i
            factors.append(i)           

    
    
    #Aqui criamos um dicionaro para conseguir os fatores e suas potências
    # do tipo (m**x).(n**y) 
    NumAndExps = dict()
    for i in factors:
        NumAndExps[i] = NumAndExps.get(i,0) + 1

    
    #Neste bloco vamos gerar os valores com as devidas potências
    dic2 = dict()
    for numero,reps in NumAndExps.items():
        dic2[numero] = dic2.get(numero,[])
        for exp in range(reps+1):
            dic2[numero].append(numero**exp)
            if numero**exp not in multiplos:
                multiplos.append(numero**exp)           

    combinadostotal = []

    fatoresmax = []

    count = 0

    
    for primein,prim in enumerate(primes):

        for i in dic2[prim]:
                for p in primes:
                    if p != prim:
                        try:
                            for w in dic2[p]:
                                templist = []
                                count = count +1
                                for j in w:
                                    temp = i*j
                                    if temp not in multiplos:
                                        multiplos.append(temp)
                                    if count == 1:
                                        fatoresmax.append(temp)                                                                   
                                        templist.append(temp)
                                    elif count > 1:
                                        templist.append(temp)
                                        for indk, k in enumerate(fatoresmax):
                                            fatoresmax[indk] = (k*j)
                                            if fatoresmax[indk] not in multiplos:
                                                multiplos.append[fatoresmax[indk]]
                                combinadostotal.append(templist)

                        except Exception:
                            continue
###### todo continuar essa loucura...

                if count > 2:
                    for listafinal in dic2.values():
                        for num in listafinal:
                                for indk, k in enumerate(fatoresmax):
                                        fatoresmax[indk] = (k*num)
                                        if fatoresmax[indk] not in multiplos:
                                            multiplos.append[fatoresmax[indk]]
                                
                                for x in combinadostotal:
                                    for y in x:
                                        temp = y * num
                                        if temp not in multiplos:
                                            multiplos.append(temp)
                else:
                    pass



        del dic2[prim]



    #algo se perdendo do caminho, precisa de pouquíssimos polimentos, está muito próximo.
    return dic2,multiplos,combinadostotal

try:
    n1 = int(input())
    while True:
        p = int(input())
        n = n1*p
        print(FireGoblet(n,p))
except:
    pass
