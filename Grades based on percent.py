while True:

    name = input("Enter your name: ")
    percent = int(input("Enter your obtained percentage: "))

    if percent <=100 and percent >=90:
        print("Grade obtained by", name, "is A+")
    elif percent <=89 and percent >80:
        print("Grade obtained by", name, "is A")
    elif percent <=80 and percent >75:
        print("Grade obtained by", name, "is B")
    elif percent <=75 and percent >60:
        print("Grade obtained by", name, "is C")
    elif percent <=60 and percent >50:
        print("Grade obtained by", name, "is D")
    elif percent <=50 and percent >=40:
        print("Grade obtained by", name, "is E")
    else:
        print("Grade obtained by", name, "is F")

    ans = input("Do you want to Continue(Yes or No) : ")
    if ans == "Yes" or ans == "yes":
        continue
    elif ans == "No" or ans == "no":
        break
