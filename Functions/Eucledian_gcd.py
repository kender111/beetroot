def eucledian_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(eucledian_gcd(a, b))

#---------------------
# from math import gcd
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(gcd(a, b))
