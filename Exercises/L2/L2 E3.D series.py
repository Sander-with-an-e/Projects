sum=0
n_max=1000000
for n in range(1,n_max):
    sum += ((-1)**n)*((2*n+1)/(3*n+2))
print(sum)

#converges to -0.6245
