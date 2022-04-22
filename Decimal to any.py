def binary(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%2
        n = n//2
        num = num+remainder*mult
        mult *=10
    return num

def octal(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%8
        n = n//8
        num = num+remainder*mult
        mult *=10
    return num

def hexadecimal(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%16
        n = n//16
        num = num+remainder*mult
        mult *=10
    return num

n = int(input("Enter the decimal no.: "))
print("In Binary: ", binary(n))
print("In Octal: ", octal(n))
print("In Hexadecimal: ", hexadecimal(n))
