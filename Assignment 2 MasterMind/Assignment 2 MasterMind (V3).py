print('I have a code with 4 colours, each different. \nEach colour is represented by a number 1 - 6, as there are 6 possible colours in\ntotal.')

print('\nAttempt to guess the code within 10 times using my feedback of your guess.\n')

import random
secret_code=random.sample(range(1,7), 4)

attempts = 0

while True:
    guess = input("Enter your guess (4 digits separated by spaces): ").strip().split()
    # Validate input
    if len(guess) != 4 or not all(num.isdigit() and 1 <= int(num) <= 6 for num in guess):
        print("Invalid input. Please enter 4 digits between 1 and 6 separated by spaces.")
        continue
    
    guess = [int(num) for num in guess]
    attempts += 1
    
    # Evaluate guess
    correct_position = 0
    correct_color = 0
    
    for i in range(len(secret_code)):
        if secret_code[i] == guess[i]:
            correct_position += 1
    
    secret_code_count = [0] * 7
    guess_count = [0] * 7
    
    for i in range(len(secret_code)):
        secret_code_count[secret_code[i]] += 1
        guess_count[guess[i]] += 1
    
    for i in range(1, 7):
        correct_color += min(secret_code_count[i], guess_count[i])
    
    correct_color -= correct_position
    
    # Print feedback
    print("Feedback: {} correct digits in the right position, {} correct digits in the wrong position.".format(correct_position, correct_color))
    
    # Check if code is guessed
    if correct_position == 4:
        print("Congratulations! You've guessed the code in {} attempts.".format(attempts))
        break
