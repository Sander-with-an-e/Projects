import math
import matplotlib.pyplot as plt
import numpy as np

g0 = -3.711 #m/s^2
ve = 4400 #m/s
kv = 0.05
CdS = 4.92 #m^2
#hT = 0.2*p #km

m_zfw = 699.0 #kg
#m_fuel = 100 #kg
#m = m_zfw + m_fuel #kg

gamma = -20 #deg

v = 262.0 #m/s
vx = math.cos(math.radians(gamma))*v #m/s
vy = math.sin(math.radians(gamma))*v #m/s
vy_ref = -2.0 #m/s

h = 20 #km
x = 0 #km

t = 0 #s
dt = 1 #s



from marsatm import marsinit, marsatm_1
marstable = marsinit()



ttab = []
htab = []
xtab = []
vtab = []
m_dottab = []
gammatab = []

for n in range(5,20):
    m_fuel = 5*n 
    m = m_zfw + m_fuel
    for p in range(5,25):
        hT = 0.2*p  
        while True:
            temp, rho, c = marsatm_1(h, marstable)
            if vx==0 or vy/vx > 10000 or vy/vx < 10000:
                gamma = -90
            
            else:
                gamma = math.degrees(math.atan(vy/vx))

            if h<hT and h>0.0003 and m_fuel>0:
                dvy = vy_ref - vy
                m_dot = min(5,((m*g0)/(ve))+kv*dvy)
        
                Tx = -m_dot*ve*math.cos(math.radians(gamma))
                Ty = -m_dot*ve*math.sin(math.radians(gamma))

                m_fuel -= m_dot*dt
            else:
                m_dot = 0
                Tx = 0
                Ty = 0
    
            Fy_g = m*g0
            Fx_drag = -CdS*0.5*rho*(v**2)*math.cos(math.radians(gamma))
            Fy_drag = -CdS*0.5*rho*(v**2)*math.sin(math.radians(gamma))
    
            Fx_tot = Fx_drag + Tx
            Fy_tot = Fy_drag + Ty + Fy_g

            ax = Fx_tot/m
            ay = Fy_tot/m

            vx += ax*dt
            vy += ay*dt
            v = math.sqrt(vx**2 + vy**2)

            x += (vx/1000)*dt
            h += (vy/1000)*dt

            if h<0:
                break

            m = m_zfw + m_fuel
    
            ttab.append(t)
            htab.append(h)
            xtab.append(x)
            m_dottab.append(m_dot)
            vtab.append(v)
            gammatab.append(gamma)

            t += dt
        print(vy)
        if vy>=-3 and vy<0:
            break
    if vy>=-3 and vy<0:
        break

plt.subplot(2,3,1)
plt.plot(xtab,htab)
plt.xlim(0,20)
plt.ylim(0,20)
plt.title('Trajectory')
plt.grid(True)

plt.subplot(2,3,2)
plt.plot(vtab,htab)
plt.ylim(0,20)
plt.xlim(0,100)
plt.title('Speed')
plt.grid(True)

plt.subplot(2,3,3)
plt.plot(ttab,m_dottab)
plt.ylim(0,5)
plt.title('Mdot vs Time')
plt.grid(True)

plt.subplot(2,3,4)
plt.plot(ttab,htab)
plt.ylim(0,20)
plt.title('Alt vs Time')
plt.grid(True)

plt.subplot(2,3,5)
plt.plot(ttab,vtab)
plt.ylim(0,500)
plt.title('Speed vs Time')
plt.grid(True)

plt.subplot(2,3,6)
plt.plot(ttab,gammatab)
plt.ylim(-90,0)
plt.title('Gamma vs Time')
plt.grid(True)

plt.show()

        
