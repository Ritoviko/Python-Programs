def binary(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%10
        n = n//10
        num = num+remainder*mult
        mult *=2
    return num

def octal(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%10
        n = n//10
        num = num+remainder*mult
        mult *=8
    return num

def hexadecimal(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%10
        n = n//10
        num = num+remainder*mult
        mult *=16
    return num


n = int(input("Enter the number: "))
b = int(input("Enter the base (2, 8 or 16): "))

if b == 2:
    print("Binary conversion to decimal: ", binary(n))
elif b==8:
    print("Octal conversion to decimal: ", octal(n))

elif b==16:
    print("Hexadecimal to decimal: ", hexadecimal(n))

elif b==10:
    print(n)

else:
    print("Wrong base")
