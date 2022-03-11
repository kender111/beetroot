import random

input_word = input('Please, input the word: ')
shuffled = random.sample(input_word, len(input_word))
print(''.join(shuffled))
