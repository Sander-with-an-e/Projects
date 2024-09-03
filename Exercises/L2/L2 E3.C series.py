import math
sum=0
n_max=1000000
for n in range(1,n_max):
    sum += ((-1)**n)*(((math.sin(n))**2)/n)
print(sum)

#converges to -0.3078
