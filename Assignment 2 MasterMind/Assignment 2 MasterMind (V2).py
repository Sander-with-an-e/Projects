print('I have a code with 4 colours, each different. \nEach colour is represented by a number 1 - 6, as there are 6 possible colours in total.')

print('\nAttempt to guess the code within 10 times using my score of your guess.\n')

import random
random.sample(range(1,7), 4)

attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = list(input(f'Guess {attempts + 1}/{max_attempts}: '))
    if guess.count('1') > 0:
    guess.count('1')
    attempts = attempts + 1
