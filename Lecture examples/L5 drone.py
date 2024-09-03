import matplotlib.pyplot as plt
import math

m = 2.0 # kg
g = 9.81 #m/s^2
dt = 0.01 # s
theta = math.radians(5)

t = 0.0 # s
x = 0.0 # m
vx = 0.0 # m/s

ttab = []
xtab = []
vxtab = []
axtab = []

for i in range(1000):
    t = t + dt

    T = g / math.cos(theta)
    
    Fx = T * math.sin(theta) 

    ax = Fx / m
    vx = vx + ax * dt
    x = x + vx * dt

    ttab.append(t)
    axtab.append(ax)
    vxtab.append(vx)
    xtab.append(x)

plt.subplot(3,1,1)
plt.plot(ttab,xtab)
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')

plt.subplot(3,1,2)
plt.plot(ttab,vxtab)
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')

plt.subplot(3,1,3)
plt.plot(ttab,axtab)
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.show()
