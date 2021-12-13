n = input("Enter any input: ")

if n >= "0" and n <= "9":
    print(n, "is integer.")
    
elif n >="a" and n <="z":
    print(n, "is small alphabet.")
    
elif n >="A" and n <="Z":
    print(n, "is capital alphabet.")

else:
    print(n, "is special character.")
