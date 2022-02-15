# Solution 1
random_string = 'My cats are the most cheeky cats in the world'
string_to_list = random_string.split() # split string into substrings
list_to_dict = dict.fromkeys(string_to_list, 0) # Assigning values to keys

for a in string_to_list: #count the number of occurrences and write to the key values
    list_to_dict[a] += 1
print(list_to_dict)

# Solution 2
from collections import Counter

random_string = 'My cats are the most cheeky cats in the world'
list_random_string = random_string.lower().split() # Coercing a string to the same case and splitting into substrings
dict_random_string = Counter(list_random_string) # Count occurrences of keys in a string

print(dict_random_string)
