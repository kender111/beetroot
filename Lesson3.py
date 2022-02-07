height, weight = 1.7, 60 #Програма як така матиме сенс, якщо замість жорстко заданих змінних задати float(input()) 
print(18.5 < (weight / height ** 2) < 25)
#
input_number = '380123456789'
check = ('380' == input_number[:3] and len(input_number) == 12 and input_number.isdigit()) # замість .isdigit() можна використати .isdecimal()
print(check)
