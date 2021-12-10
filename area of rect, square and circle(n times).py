print("Whose area you want to find: ")
print("1. Area of circle")
print("2. Area of square")
print("3. Area of rectangle")

count = int(input("How many times do you want to run the program: "))
print("----------------------------------------------------------------------------")

#i = 0

for i in range(0, count):
#while i < count:
    n = int(input("Select an option (1, 2 or 3): "))

    if n == 3:
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        area_rect = length*breadth
        print("Area of the rectangle: ", area_rect, "sq unit")
        print("----------------------------------------------------------------------------")

    elif n == 2:

        a = int(input("Enter the side of the square: "))
        area_sq = a**2
        print("Area of the square: ", area_sq, "sq unit")
        print("----------------------------------------------------------------------------")

    elif n == 1:

        r = int(input("Enter the radius of the circle: "))
        area_circle = 3.14 * (r**2)
        print("Area of circle: ", area_circle, "sq unit")
        print("----------------------------------------------------------------------------")

    else:
        print("Invalid option")
        print("----------------------------------------------------------------------------")
    #i+=1
