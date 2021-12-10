while True:

    print("Whose area you want to find: ")
    print("1. Area of rectangle")
    print("2. Area of square")
    print("3. Area of circle")
    print("4. Exit")

    n = int(input("Select an option (1, 2 or 3): "))

    if n == 1:
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

    elif n == 3:

        r = int(input("Enter the radius of the circle: "))
        area_circle = 3.14 * (r**2)
        print("Area of circle: ", area_circle, "sq unit")
        print("----------------------------------------------------------------------------")

    elif n == 4:
        break

    else:
        print("Invalid option")
