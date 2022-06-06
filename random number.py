import random

a_list = []
def show_score():
    if len(a_list)<0:
        print("There is no high score currently ")
        print("------------------------------")
    else:
        print("The Highest score is in ", min(a_list), " attempts.")
        print("------------------------------")


attempt = 0
choice = input("Do you want to Play? (yes/no): ")
print("------------------------------")
num = int(random.randint(1, 10))
if choice.lower()=="yes":
    while True:
        guess = int(input("Guess a number between 1 to 10: "))
        print("------------------------------")

        if guess<1 or guess>10:
            print("Choose the number within the range.")
            print("------------------------------")

        elif guess>num:
            print("Hint: its lower")
            print("------------------------------")
            attempt +=1
        elif guess<num:
            print("Hint: its higher")
            print("------------------------------")
            attempt +=1
        elif guess==num:
            print("Correct guess")
            print("It was ", num)
            print("------------------------------")
            attempt+=1
            a_list.append(attempt)
        
            print("You Got it in ", attempt, " attempts.")
            print("------------------------------")
            opt = input("Do you wanna Play again?")
            if opt.lower()=="yes":
                attempt = 0
                num = int(random.randint(1, 10))
            else:
                print("Ok")
                print("------------------------------")
                opt2 = input("Do you want to see the highscore so far??")
                if opt2.lower()=="yes":
                    show_score()
                    print("------------------------------")
                    break
                else:
                    print("Have a good day")
                    print("------------------------------")
                    break
            
else:
    print("Ok, that's cool")
    print("------------------------------")

