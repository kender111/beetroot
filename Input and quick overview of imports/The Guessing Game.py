import random

player_digit = int(input('Please, enter a number from 1 to 10: '))

if 1 <= player_digit <= 10:
    computer_digit = random.randint(1, 10)
    if computer_digit < player_digit or computer_digit > player_digit:
        print(f'I\'m win! Correct number: {computer_digit}')
    elif computer_digit == player_digit:
        print('Great! You guessed it!')
else:
    print('Incorrect data, the game is over')
