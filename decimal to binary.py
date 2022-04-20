def binary(n):
    num = 0
    mult = 1
    while n>0:
        remainder = n%2
        n = n//2
        num = num+remainder*mult
        mult *=10
    return num


n = int(input())

print(binary(n))
