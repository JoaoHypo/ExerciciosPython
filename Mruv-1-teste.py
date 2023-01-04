'''
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
    a = a*pi/180

    #torricieli para achar a velocidade final em y0
    Vyf = sqrt((sin(a)* v0)**2 + 2*-g*(0 - h))

    #achando tempo
    t = (sin(a)*v0 - Vyf) / g

    #encontrando xf deste cenário
    xf = x0 + cos(a)*v0*t

    if round(xf) == x1:

        return round(xf,5) , '-> DUCK'
    else:
        return round(xf,5) ,'-> NUCK'

try:
    h = float(input())
    x0,x1 =  (int(i) for i in input().split())
    ntrys = int(input())

    for i in range(ntrys):

        a,v0 =  (float(i) for i in input().split())
        print(AngryDucks(h,x0,x1,a,v0))
except:
    pass
