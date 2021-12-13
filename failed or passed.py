name = input("Name: ")

print("Enter the marks: ")

maths = int(input("Maths: "))
eng = int(input("English: "))
sci = int(input("Science: "))
it = int(input("IT: "))

percentage = ((maths+eng+sci+it)/200)*100

#print("Total Percentage scored: ", percentage)

if percentage >= 65:
    print("Pass")

else:
    print("Fail")
