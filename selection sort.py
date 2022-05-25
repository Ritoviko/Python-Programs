def SelectSort(a):
    for k in range(len(a)):
        mini = a[k]
        for i in range(k, len(a)):
            if mini>a[i]:
                mini = a[i]
        for i in range(k ,len(a)):
            if a[k] > mini and a[i]==mini:
                temp = a[i]
                a[i]=a[k]
                a[k]=temp
                break
                
    

n = int(input("Enter the size of the array: "))
a = []
print("Enter the elements of the array: ")
for i in range(n):
    a.append(int(input()))
print(a)
SelectSort(a)
print(a)

