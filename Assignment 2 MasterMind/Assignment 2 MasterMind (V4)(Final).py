print('*** MasterMind ***\n\n')
print('I have a code with 4 colours, each different. \nEach colour is represented by a number 1 - 6, as there are 6 possible colours in total.')

print('\nAttempt to guess the code within 10 times using my feedback of your guess.\n')

import random
secret_code=random.sample(range(1,7), 4)
secret_code
n=1

while True:
    guess = input(f"guess {n}: ")
    #guess = [int(guess[0]),int(guess[1]),int(guess[2]),int(guess[3])]
    guess = [int(num) for num in guess]
    if len(guess) != 4 or guess.count(0)>0 or guess.count(7)>0 or guess.count(8)>0 or guess.count(9)>0 or guess.count(1)>1 or guess.count(2)>1 or guess.count(3)>1 or guess.count(4)>1 or guess.count(5)>1 or guess.count(6)>1:
        print('Invalid entry! Try again!')
    else:    
    
        correct_position = 0 
        correct_colour = 0

        for i in range(4):
            if secret_code[i] == guess[i]:
                correct_position += 1

        for k in range(1,7):
            if k in secret_code:
                if k in guess:
                    if secret_code.index(k) != guess.index(k):
                        correct_colour = correct_colour + 1
            
        print(f'Correct numbers: {correct_position}')
        print(f'Correct numbers in wrong position: {correct_colour}')

    
    
        if correct_position == 4:
            print(f'Well done! The secret code was indeed {secret_code}.')
            play_again = input('Do you want to play again (y/n)?:')
            if play_again == 'yes' or play_again == 'y' or play_again == '':
                n=0
                secret_code=random.sample(range(1,7), 4)
                #print(secret_code)
            else: break

        if n == 10:
            print(f'You did not guess the code! The code was {secret_code}.')
            play_again = input('Do you want to play again (y/n)?:')
            if play_again == 'yes' or play_again == 'y' or play_again == '':
                n=0
                secret_code=random.sample(range(1,7), 4)
                #print(secret_code)
            else: break

        n += 1


    
