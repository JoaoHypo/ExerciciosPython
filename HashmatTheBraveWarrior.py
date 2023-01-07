'''
Hashmat the Brave Warrior
Hashmat is a brave warrior who with his group of young soldiers moves from one place to another to fight against his opponents. Before fighting he just calculates one thing, the difference between his soldier number and the opponent's soldier number. From this difference he decides whether to fight or not. Sometimes Hashmat's soldier number is greater than his opponent.

Input
The input contains two integer numbers in every line. These two numbers in each line denotes the number of soldiers in Hashmat's army and his opponent's army or vice versa. The input numbers are not greater than 232. Input is terminated by End of File.

Output
For each line of input, print the difference of number of soldiers between Hashmat's army and his opponent's army. Each output should be in seperate line.

Input Sample	
10 12
10 14
100 200

Output Sample
2
4
100
'''


try:
    while True:
        x0,x1 =  (int(i) for i in input().split())
        print(abs(x1-x0))
except:
    pass
