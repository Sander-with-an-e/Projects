# simulate for 20 seconds a falling, bouncing ball
import numpy as np
from matplotlib import pyplot as plt

# parameters
m = 1
g = 9.81
R = 1
dt = 0.001
t_end = 20

# initial conditions
x = np.asarray([0.00001,0.8])
v = np.asarray([0,0])
a = np.asarray([0,-g]) #because m = 1 Fg = g
t = 0

x_crossings = 0
y_crossings = 0

x_tab = []
y_tab = []

while t <= t_end:

    # for plotting
    x_tab.append(x[0])
    y_tab.append(x[1])

    # keep track of the previous one
    x_prev = x
    
    # update velocity
    v = v + a * dt
    x = x + v * dt

    if x[0] >= 0 and x_prev[0] < 0:
        y_crossings += 1 #he said x_crossings here but I think thats wrong
    if x[0] < 0 and x_prev[0] >= 0:
        y_crossings += 1 #he said x_crossings here but I think thats wrong
    if x[1] >= 0 and x_prev[1] < 0:
        x_crossings += 1 #he said y_crossings here but I think thats wrong
    if x[1] < 0 and x_prev[1] >= 0:
        x_crossings += 1 #he said y_crossings here but I think thats wrong

    # detect and deal with collision
    if np.linalg.norm(x) >= R:
        v_out = v - 2*((np.dot(v,x))/(np.dot(x,x)))*x
        v = v_out

    # increment time
    t += dt

print(f'x-crossings = {x_crossings}, y-crossings = {y_crossings}')

plt.figure()
plt.plot(x_tab,y_tab)
plt.show()
