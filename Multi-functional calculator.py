while True:
    print("MAIN MENU")
    print("1. Calculator")
    print("2. Area Finder")
    print("3. Volume Finder")
    print("4. Exit")
    opt1 = int(input("Enter your option: "))
    print("--------------------------------------------------------")

    if opt1 == 1:
        while True:
            print("CALCULATOR")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            opt2 = int(input("Enter your option: "))
            print("--------------------------------------------------------")

            if opt2 == 1:
                print("ADDITION")
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))

                add = a+b

                print("The sum of ", a,"and", b, "is", add)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 2:
                print("SUBTRACTION")

                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))

                sub = a-b

                print("The difference between", a, "and", b, "is", sub)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 3:
                print("MULTIPLICATION")

                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))

                mult = a*b

                print("The Multiplication of", a, "and", b, "is", mult)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 4:
                print("DIVISION")

                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))

                div = a/b

                print("The division of", a, "by", b, "is", div)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            else:
                print("Enter a valid/ available option")
                continue

    elif opt1==2:
        while True:
            print("AREA FINDER")
            print("1. Square")
            print("2. Rectangle")
            print("3. Triangle")
            print("4. Circle")

            opt2 = int(input("Enter any option: "))
            print("--------------------------------------------------------")

            if opt2 == 1:
                print("AREA OF SQUARE")

                a = int(input("Enter the side of square: "))

                area = a**2
                print("Area of square = ", area)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 2:
                print("AREA OF RECTANGLE")

                length = int(input("Enter the length of the rectangle: "))
                breadth = int(input("Enter the breadth of the rectangle: "))

                area = length*breadth
                print("Area of rectangle = ", area)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 3:
                print("AREA OF TRIANGLE")

                base = int(input("Enter the base of triangle: "))
                height = int(input("Enter the height of the triangle: "))

                area = (base*height)/2
                print("Area of triangle = ", area)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 4:
                print("AREA OF CIRCLE")

                r = int(input("Enter the radius of the circle: "))

                area = 3.14*r*r
                print("Area of circle = ", area)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            else:
                print("Enter the valid option.")
                continue

    elif opt1==3:
        while True:
            print("VOLUME FINDER")
            print("1. Sphere")
            print("2. Cylinder")
            print("3. Cone")

            opt2 = int(input("Enter any option: "))
            print("--------------------------------------------------------")

            if opt2 == 1:
                print("VOLUME OF SPHERE")

                r = int(input("Enter the radius of sphere: "))

                volume = (4/3)*(3.14*(r**3))
                print("Volume of sphere = ", volume)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 2:
                print("VOLUME OF CYLINDER")

                r = int(input("Enter the radius of the cylinder: "))
                h = int(input("Enter the height of the cylinder: "))

                volume = 3.14*r*r*h
                print("Volume of cylinder = ", volume)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            elif opt2 == 3:
                print("VOLUME OF CONE")

                r = int(input("Enter the radius of the cylinder: "))
                h = int(input("Enter the height of the cylinder: "))

                volume = (3.14*r*r*h)/3
                print("Volume of cone = ", volume)
                print("--------------------------------------------------------")

                choice = input("Do you want to go to the MAIN MENU? <y/n>: ")
                if choice == "y":
                    print("--------------------------------------------------------")
                    break
                elif choice == "n":
                    print("--------------------------------------------------------")
                    continue

            else:
                print("Enter the valid option.")
                continue

    elif opt1==4:
        print("Thank you for the service.")
        break

    else:
        print("Please enter a valid option!!")
        print("--------------------------------------------------------")
