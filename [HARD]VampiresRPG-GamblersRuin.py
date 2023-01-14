'''
Vampires RPG - Gambler's Ruin
Felipinho is thrilled with his new RPG game, about wars between clans of vampires. In this game he plays a vampire that repeatedly comes into combat against vampires from other clans. Such battles are won or lost based on some characteristics of the opponents, with the help of a standard six-faced dice. For simplicity, we will consider only the fight between two vampires, Vampire 1 and Vampire 2. Each vampire has a vital energy (denoted respectively by EV1 and EV2). Besides, an attack force AT and a damage capacity D are also given.

The combat is fought in turns, in the following way. At each turn, the dice is rolled; if the result value is less than or equal to AT, Vampire 1 wins the turn, otherwise Vampire 2 wins. The winner then sucks the value D from the loser\'s vital energy. That is, D points are subtracted from the loser's vital energy and added to the winner's vital energy. The combat continues until one of the fighters has EV less than or equal to zero.

For example, suppose EV1=7, EV2=5, AT=2 and D=4. The dice is rolled and the result value is 3. Then, Vampire 2 wins the turn, and therefore 4 points are subtracted from EV1 and added to EV2. The new values for the vital energies would be EV1=3 and EV2=9. Notice that, if in the next turn Vampire 2 wins again, the combat ends. The values of AT and D are constant throughout the combat; only EV1 and EV2 vary.

Despite loving the game, Felipinho thinks that the combats are too long, and suspects that, given the initial values of EV1, EV2, AT and D, it is possible to determine the probability of one of the players winning the combat, and that could help shorten the combat time. Felipinho has asked your help to verify his suspicion.

Input
The input contains several test cases. Each test case is given in one single line, containing four integers EV1, EV2, AT and D separated by spaces (1 ≤ EV1, EV2 ≤ 10, 1 ≤ AT ≤ 5 and 1 ≤ D ≤ 10). The end of input is indicated by one line containing only four zeros, separated by spaces.

Output
For each test case in the input, your program must print a single line. The line must contain a real number representing, in terms of percentages, the probability that Vampire 1 wins the combat. The result must be printed as a real number with exactly one decimal figure.

Input Sample
1 1 3 1
1 2 1 1
8 5 3 1
7 5 2 4
0 0 0 0

Output Sample
50.0
3.2
61.5
20.0
'''

# Energia Vital = 1 ≤ EV1, EV2 ≤ 10

#Attack Force = 1 ≤ AT ≤ 5

#Damage Capacity = 1 ≤ D ≤ 10

# Gambler's Ruin: https://en.wikipedia.org/wiki/Gambler's_ruin
                 #https://www.youtube.com/watch?v=Ne2lmAZI4-I&ab_channel=MITOpenCourseWare 

def Vamp1Win(Ev1, Ev2, Atf, Dc):

    # Convertendo força vital para chances probabilisticas
    # (Quantos vezes o vampira tanka o dano, lembrando que Ev pode ser < 0 em combate)
    if Ev2%Dc > 0:
        Ev2 = (int((Ev2/Dc)+1))  # Aqui garante que caso haja resto na divisão, o dano conte igual
    else:
        Ev2 = int(Ev2/Dc)  # Para valores exatos

    # Para Ev1
    if Ev1%Dc > 0:
        Ev1 = (int((Ev1/Dc)+1))
    else:
        Ev1 = int(Ev1/Dc)

    # Prob do jogador 1 quando o dado é justo 50/50
    if Atf == 3:
        diceprob = Ev1/(Ev1+Ev2)

    # Probabilidade estatística do segundo jogador zerar seu valor
    else:
        p = Atf/6
        q = 1 - p
        diceprob = (1 - ((q/p)**(Ev1)))/(1 - ((q/p)**(Ev1+Ev2)))

    return round(float(diceprob)*100, 1) 

while True:

    Ns = [int(x) for x in input().split()]
    if Ns == [0, 0, 0, 0]:
        break
    else:
        print(Vamp1Win(Ns[0], Ns[1], Ns[2], Ns[3]))
