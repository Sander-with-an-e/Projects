print('I have a code with 4 colours, each different. \nEach colour is represented by a number 1 - 6, as there are 6 possible colours in total.')

print('\nAttempt to guess the code within 10 times using my score of your guess.\n')

import random
print(random.sample(range(1,7), 4))

guess_1=list(input('Guess 1: '))
print(f"[{', '.join(guess_1)}]")
i=1
while i<7:
    print(guess_1.count("'i'"))
    if guess_1.count("'i'") > 0:
        print(guess_1.index("'i'"))
    i=i+1
    print('\n')

for i in range(1,7):
    print(guess_1.count(i))   
    if guess_1.count(i) > 0:
        print(guess_1.index(i))
    print('\n')

guess_1.count('1')
if guess_1.count('1') > 0:
    guess_1.index('1')

guess_1.count('2')
if guess_1.count('2') > 0:
    guess_1.index('2')   

guess_1.count('3')
if guess_1.count('3') > 0:
    guess_1.index('3')

guess_1.count('4')
if guess_1.count('4') > 0:
    guess_1.index('4')     

guess_1.count('5')
if guess_1.count('5') > 0:
    guess_1.index('5')

guess_1.count('6')
if guess_1.count('6') > 0:
    guess_1.index('6')    
