def decimal(n):
    num =0
    mult = 1
    while n>0:
        rem = n%10
        n = n//10
        num = num+rem*mult
        mult *=2
    return num

def octal(n):
    num =0
    mult = 1
    while n>0:
        rem = n%8
        n = n//8
        num = num+rem*mult
        mult *=2
    return num

def hexa(n):
    num =0
    mult = 1
    while n>0:
        rem = n%16
        n = n//16
        num = num+rem*mult
        mult *=2
    return num


n = int(input("Enter the binary number: "))
print("In decimal: ", decimal(n))
print("In Octal: ",octal(n))
print("In Hexadecimal: ",hexa(n))
