from random import randint

random_number_list = []
while len(random_number_list) <= 9: # create a list of random numbers of length 10
    random_number_list.append(randint(-1000, 1000))
print(random_number_list) # Checking list values
#get the largest number of a list using a function max
print(max(random_number_list))

# getting the largest value of a list with a loop while
index_number = 0 
maximum = random_number_list[index_number]

while index_number < len(random_number_list) - 1:
    index_number += 1
    if maximum < random_number_list[index_number]:
        maximum = random_number_list[index_number]

print(maximum)
