#Méodo de Passo Variável

def RK2(x,v,dt,):
    return
def RK4(x,v,dt):
    return

x_list = []
v_list = []
t_list = []

tolerancia = None
dt = None
tf,t = 200,0
count = 0
limit_count = 0
n = 0
while t < tf:
    count += 1
    x,v = RK2(x,v,dt,t)
    xa,va = x,v
    t += dt
    if count%limit_count == 0:
        xp,vp = RK4(xa,va,dt,t)
        ecx = abs(x - xp)
        ecv = abs(v- vp)
        ec = max(ecx,ecv)
        dtnovo = dt*((tolerancia/ec)**1/n)
        
        if dtnovo > 2*dt: dt = 2*dt
        if dtnovo < dt/2: dt = dt/2

    x_list.append(x)
    v_list.append(v)
    t_list.append(t)
