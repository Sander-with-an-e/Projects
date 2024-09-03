n=int(input('Enter the value of n:'))
k=int(input('Enter the value of k:'))

numerator=1
denominator=1

if k<=0:
    print('NA')   
else:
    for i in range(k):
        numerator=numerator*(n-i)
    for i in range(k):
        denominator=denominator*(k-i)
    n_over_k=numerator/denominator
    print(f'n over k = {n_over_k}')
