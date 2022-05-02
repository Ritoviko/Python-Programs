import numpy as np

n = int(input("Row value: "))
m = int(input("Column value: "))
a = np.full([n,m], 1)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        x = int(input())
        a[i][j] = x
print(a)

minrow=0
mincol=0
maxrow=len(a)-1
maxcol=m-1

tne = n*m

count =0

while count<tne:

    if count<tne:
        for i in range(minrow, maxrow+1):
            print(a[i][mincol])
            count+=1
    mincol+=1
    
    if count<tne:
        for j in range(mincol, maxcol+1):
            print(a[maxrow][j])
            count+=1
    maxrow-=1

    if count<tne:
        for i in range(maxrow, minrow-1,-1):
            print(a[i][maxcol])
            count+=1
    maxcol-=1

    if count<tne:
        for j in range(maxcol, mincol-1, -1):
            print(a[minrow][j])
            count+=1
    minrow+=1

    
