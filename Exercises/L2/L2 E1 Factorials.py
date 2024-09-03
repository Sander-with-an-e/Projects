n=int(input('Enter the value of which you want the factorial calculated:'))

#WHILE loop:
i=1
factorial=1
if n<0:
    print(f'{n}! cannot be calculated.')
elif n==0:
    print(f'{n}! = 0')
else:
    while i<=n:
        factorial=factorial*i
        i=i+1      
    print(f'{n:1d}! = {factorial}')

#FOR loop:
factorial=1
if n<0:
    print(f'{n}! cannot be calculated.')
elif n==0:
    print(f'{n}! = 0')
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(f'{n}! = {factorial}')
        
    
    

