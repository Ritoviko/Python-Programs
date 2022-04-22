import array as a

n = int(input("Enter the size of the array: "))
arr = a.array('i')
print("Enter the values of the array: ")

for i in range(n):
    m = int(input())
    arr.append(m)
'''
x =max(a)
y = min(a)
'''
x= arr[0]
y = arr[0]
for i in (arr):
    if x<i:
        x = i
    elif y>i:
        y = i

span = x-y

print("Span of array is: ")
print(span)
