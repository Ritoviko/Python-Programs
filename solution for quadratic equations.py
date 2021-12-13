a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

D = 4*a*c - 2
sqrt_D = D**0.5

d = (b**2 + sqrt_D)/(2*a)

print("The solution of the equation is: ", d)
