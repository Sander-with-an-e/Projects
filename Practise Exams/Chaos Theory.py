import math
import numpy as np

m = 1 #kg
g = -9.81 #m/s^2
R = 1 #m
dt = 0.001 #sec
t_end = 20.0 #sec
x = np.array([0.00001,0.8])
v = np.array([0,0])
t = 0
x_axis_pass = 0
y_axis_pass = 0

running = True
while running:
    Fg = m * g

    a = np.array([0,Fg/m])
    #print(f'a = {a}')
    dv = np.array([0,Fg*dt/m])
    v = np.add(v,dv)
    #print(v)
    
    if math.sqrt(x[0]**2 + x[1]**2) == 1:
        dv_1 = (np.dot(v,x))/(np.dot(x,x))
        dv_2 = []
        for i in x:
            dv_2.append(-i*2*dv_1)
        v = np.add(v,dv_1)
        
        
   
    dx = np.array([v[0]*dt,v[1]*dt])
    x = np.add(x,dx)

    if x[0] == 0:
        y_axis_pass += 1
    if x[1] == 0:
        x_axis_pass += 1
    t = t + dt
       
    if t == t_end:
        break
print(y_axis_pass)
print(x_axis_pass)
