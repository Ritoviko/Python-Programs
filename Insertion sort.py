def insertion(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp

n = int(input("Enter the size of the array: "))
a = []

print("Enter the elements of  the array: ")
for i in range(n):
    a.append(int(input()))
print(a)
insertion(a)

print("Increasing order: ")
print(a)
print("Decreasing Order: ")
print(a[::-1])


