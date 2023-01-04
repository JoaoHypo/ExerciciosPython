'''

Angry Ducks

In a far away land there are two cities, Nlogony, home of the Nlogonies, 
and Ducklogony, home of their neighbors, the Ducknese. These two cities 
have been at war for some time and now, in a try to win the war, the Ducknese 
intend to attack Nlogony with a slingshot that fires ducks. However, to avoid
mistakes, they asked you to build a program that, given the values of the 
slingshot's height (h), the points where the Nlogony city begins (p1) and ends 
(p2), the shooting angle (α) and the launching speed, calculates if the projectile 
will hit the target.

For the calculations, assume that the gravity's acceleration is g=9,80665 and that π = 3,14159.

Input
There are various test cases, where each one starts with 1 floating point value h( 1 ≤ h ≤ 150) 
indicating the slingshot's height, containing, in the next line, 2 integer values p1 and 
p2( 1 ≤ p1, p2 ≤ 9999) indicating where Nlogony begins and ends, the next line containing 
1 integer n(1 ≤ n ≤ 100) indicating the number of tries that will be made to hit the Nlogony
and the n following lines containing 2 floating point values indicating the values of the
launching's angle α(1 ≤ α ≤ 180) and speed V(1 ≤ V ≤ 150).

The end of the input file is determined by EOF.

Output
For each shoot, your program must print a single line in the following format:
“X -> DUCK” for when the duck hits Nlogony or “X -> NUCK” where the duck doesn't 
hit Nlogony, where X is the maximum distance that the projectile reached until
reaching the ground (y = 0). X must be printed with an accuracy of 5 decimal places.

Input Sample
2.1
368 380
3
42.3 60
30 55
44 60.876842

Output Sample
367.76208 -> NUCK
270.72675 -> NUCK
379.83781 -> DUCK

-------------------------------------------------------

Teoria que me salvou:
https://www.omnicalculator.com/physics/projectile-motion

------------------------------------------------------
h = altura
x0 = p1
x1 = p2

n = numero de tentativas
a = angulo
v = velocidade

'''

def AngryDucks(h,x0,x1,a,v0):

    from math import sin,cos,sqrt

    g = 9.80665 #gravidade
    pi= 3.14159
    theta = a*pi/180 #conversão pra rad

    #tempo de voo (tempo subida + descida com h inicial !=0 algebrado)
    t = ((v0*sin(theta)) + sqrt(((v0 * sin(theta))**2) + 2 * g * h)) / g
    
    #range, x max lançamento
    xf = cos(theta)*v0*t

    if round(xf) == x1:

        return (str(round(xf,5))+' -> DUCK')
    else:
        return (str(round(xf,5))+' -> NUCK')

try:
    while True:
        h = float(input())
        x0,x1 =  (int(i) for i in input().split())
        ntrys = int(input())

        for i in range(ntrys):
            a,v0 =  (float(i) for i in input().split())
            print(AngryDucks(h,x0,x1,a,v0))

except:
    pass
