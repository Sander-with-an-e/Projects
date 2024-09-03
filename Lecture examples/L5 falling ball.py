import matplotlib.pyplot as plt

m = 2.0
g = 9.81
dt = 0.01

t = 0.0
y = 10.0
vy = 0

ttab = []
ytab = []

while True:
    t = t + dt

    F = m * g

    a = -F / m
    vy = vy + a * dt
    y = y + vy * dt

    ttab.append(t)
    ytab.append(y)
    if y <= 0:
        break

plt.plot(ttab,ytab)
plt.title('Falling Ball')
plt.show()
