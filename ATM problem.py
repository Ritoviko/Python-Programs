total_amt = 3500000
password = 8888
i = 1
while i>0:
    print("Welcome to SAITM bank!")
    print("-------------------------------------------------")
    print("Choose any one option: ")
    print("1. Withdraw Money")
    print("2. Update Password")
    print("3. Exit")
    print("-------------------------------------------------")
    opt = int(input("Enter your option(1, 2 or 3): "))
    print("-------------------------------------------------")
    if opt == 1:
        withdraw= int(input("How much money do you want to Withdraw ? "))
        print("-------------------------------------------------")
        print("Please collect your money.")
        print("-------------------------------------------------")
        total_amt = total_amt - withdraw
        x = input("Do you want to see your total balance? (y/n): ")
        if x == "y":
            print(total_amt)
            print("-------------------------------------------------")
        else:
            continue
    elif opt == 2:
        pwrd = int(input("Enter your current password"))
        print("-------------------------------------------------")
        if pwrd == password:
            p1 = int(input("Enter your new password: "))
            p2 = int(input("Confirm your new password: "))
            print("-------------------------------------------------")
            password = p1

            print("Your password has been updated!", password)
            print("-------------------------------------------------")
        else:
            print("Your password do not match.")
            print("Please re-check your password.")
            print("-------------------------------------------------")
    elif opt == 3:
        print("Thank you for your service.")
        print("-------------------------------------------------")
        break
    else:
        print("Invalid Option")
        print("-------------------------------------------------")
        
