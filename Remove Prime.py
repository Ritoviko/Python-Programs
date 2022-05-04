import array as a

def prime(m):
    if m==0 or m==1:
        return True
    else:
        for i in range(2, m):
            if m%i==0:
                return True
        else:
            return False

arr = a.array('i', [3, 12, 13, 15])
arr1 = a.array('i')
flag = 0
for i in arr:
    if prime(i)==True:
        arr1.append(i)
print(arr1)
