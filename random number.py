import random
a_list = []

def show_score():
    if len(a_list)<0:
        print("There is no high score currently ")
    else:
        print("The Highest score is in ", min(a_list), " attempts.")


attempt = 0
choice = input("Do you want to Play? (yes/no): ")
num = int(random.randint(1, 10))
while choice.lower() == "yes":
    guess = int(input("Guess a number between 1 to 10: "))

    if guess<1 or guess>10:
        print("Choose the number within the range.")

    elif guess>num:
        print("Hint: its lower")
        attempt +=1
    elif guess<num:
        print("Hint: its higher")
        attempt +=1
    elif guess==num:
        print("Correct guess")
        print("It was ", num)

        attempt+=1
        a_list.append(attempt)
        opt = input("Do you wanna Play again?")
        if opt.lower()=="yes":
            attempt = 0
            num = int(random.randint(1, 10))
            print("So far..")
            show_score()
        else:
            print("Have a good day!")
            break
    else:
        print("Ok, that's cool")
        break
