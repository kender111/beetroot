import random

input_word = input()
shuffled = random.sample(input_word, len(input_word))
print(''.join(shuffled))
