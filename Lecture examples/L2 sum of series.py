#calculate the sum of the formula:
sum=0
k_max=1000
for k in range(k_max):
    sum=sum+(-1)**k * (4/(2*k+1)) #or you can use sum+=(-1)**k * (4/(2*k+1))

print('Outcome = ',sum)
