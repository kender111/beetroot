#BMI
height, weight = 1.7, 60 # The program as such will make sense if instead of the set variables to set float (input ())
print(18.5 < (weight / height ** 2) < 25)
#Valid_Number
input_number = '380123456789'
check = ('380' == input_number[:3] and len(input_number) == 12 and input_number.isdigit()) # замість .isdigit() можна використати .isdecimal()
print(check)
#input_number = '380123456789' # if don*t use and
#check1 = '380' == input_number[:3]
#check2 = len(input_number) == 12
#check3 = input_number.isdigit()
#print(bool(check1) == bool(check2) == bool(check3))
