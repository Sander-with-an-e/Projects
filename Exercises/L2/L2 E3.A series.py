sum=0
n_max=10
factorial=1
for n in range(1,n_max):
    for i in range(1,n+1):
        factorial=factorial*i
    sum += ((2**n)*factorial)/(n**n)
print(sum)

#diverges to +infinity
