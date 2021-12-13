n = int(input("Enter the amount of unit consumed: "))
if n<=100:
    print("Your total electricity bill = No Charge")

elif n>100:
    
    if n<200:
        i = n-100
        bill = i*5
        print("Your total electricity bill = Rs.", bill)
        
    elif n==200:
        bill = 100*5
        print("Your total electricity bill = Rs.", bill)
        
    else:
        bill = 100*5
        i = n-200
        total = bill + (i*20)
        print("Your total electricity bill = Rs.", total)
