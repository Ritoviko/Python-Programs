s = input()
print(s)
s1 = ""
'''
x = s.upper()
y = s.lower()
print(x)
print(y)
'''
for i in range(len(s)):
    if (s[i]>='a' and s[i]<='z'):
        s1 = s1+ chr(ord(s[i])-32)
        
    elif(s[i]>='A' and s[i]<='Z'):
        s1 = s1+ chr(ord(s[i])+32)

    else:
        s1 = s1+s[i]
'''
or
for i in s:
    if i.isupper():
        s1 = s1+i.lower()
    elif i.islower():
        s1 = s1+i.upper()
    else:
        s1 = s1+i
'''

print(s1)
