import random

print('Let\'s play a game... If you earn 15 points, you are win')
username = input('Please, tell me your name: ')
count = 0

while -15 < count < 15:
    actions = ('+', '-', '*')
    digit1 = random.randint(10, 20)
    digit2 = random.randint(1, 10)
    action = random.choice(actions)

    if action == '+':
        correct_answer = digit1 + digit2
    elif action == '-':
        correct_answer = digit1 - digit2
    elif action == '*':
        correct_answer = digit1 * digit2

    print(f'Your count: {count}')
    print('What is ' + str(digit1) + action + str(digit2) + '? ')
    users_answer = int(input())
    if correct_answer == users_answer:
        count += 1
        print('Correct! You are a math genius!')

    elif correct_answer != users_answer:
        count -= 1
        print(f'No! You made a mistake! Correct answer: {correct_answer}')

if count == -15:
        print(f'You loser, {username}!')
else:
    print(f'{username}, You\'ve got all the points in the world! CONGRATULATIONS!!!')
