height, weight = float(input()), float(input())
print(18.5 < (weight / height ** 2) < 25)
#
input_number = '380123456789'
check = ('380' == input_number[:3] and len(input_number) == 12 and input_number.isdigit())
print(check)