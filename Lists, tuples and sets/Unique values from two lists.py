from random import randint

first_random_list = []
second_random_list = []
while len(first_random_list) <= 9: # create a first list of random numbers
    first_random_list.append(randint(1, 10))
print(first_random_list) # Checking list values

while len(second_random_list) <= 9: # create a second list of random numbers
    second_random_list.append(randint(1, 10))
print(second_random_list) # Checking list values

unique_list = list(set(first_random_list + second_random_list))  # getting unique values using a set
print(unique_list)




