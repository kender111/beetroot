# 2

height, weight = 1.65, 60
bmi = weight / height ** 2

if bmi < 18.5:
    print('Your BMI is less than normal')
elif bmi > 25:
    print('Your BMI is greater than normal')
else:
    print('Your BMI is normal')

# 3

major_version = 3
minor_version = .9
version = major_version + minor_version
language = 'Python'
language_version = language + ' ' + str(version)

# 4

sum_less_100 = 0
number = 0

while number < 100:
    if number % 3 == 0 and number % 5 == 0:
        sum_less_100 += number
        number += 1
    else:
        number += 1
        
# 5 

surname = 'Beseda'
digit_surname = len(surname)
factorial = 1

while digit_surname > 1:
    factorial *= digit_surname
    digit_surname -= 1

print(f'{len(surname)}! = {factorial}')

# 6

task_string = 'I have a beautiful cat!'
lenght_string = len(task_string)

while lenght_string > 0:
    print(task_string[:lenght_string])
    lenght_string -= 1
else:
    print('Nothing\'s left here')
    
# Advanced

# 3 - Можливо неправильно зрозуміла задачу?

input_integer = 105
possible_prime = 2

while possible_prime < input_integer + 1:
    is_prime = True
    num = 2  
    while num < possible_prime:
        if possible_prime % num == 0:
            is_prime = False
            break
        num += 1
        
    if is_prime:
        print(possible_prime)
    possible_prime += 1
    
# 4

first = 1
second = 1
limitation = 100000
sum_num = 2

while second <= limitation:
    new_first = first + second
    first = second
    second = new_first
    while new_first % 2 == 1:
        sum_num += new_first
        break
        
print(sum_num)

# LMS_Homework

# Task 1

sample = 'helloworld'
lenght_sample = len(sample)

if len(sample) >= 2:
    print(sample[0:2] + sample[-2:] )
else:
    print('')
    
# Task 2

input_number = '0123456789'
check = (len(input_number) == 10 and input_number.isdigit()) # замість .isdigit() можна використати .isdecimal()

if check is True:
    print('Phone number is Valid')
else:
    print('Phone number is Invalid')
    
# Task3

true_name = 'kender'
input_name = 'Kender'  # input('Please, input your name: ')
print(bool(input_name.lower() == true_name.lower()))

