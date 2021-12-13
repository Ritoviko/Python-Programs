amount = int(input("Enter the amount of the item: "))

if amount < 1000:
    discount1 = amount*(5/100)
    net_amount1 = amount - discount1
    print("Amount less than 1000, 5% discount applied.")
    print("Net payable amount: ", net_amount1)

elif amount > 4000 and amount < 5000:

    discount2 = amount*(10/100)
    net_amount2 = amount - discount2
    print("Amount is between 4000 and 5000, 10% disount applied")
    print("Net payable amount: ", net_amount2)

else:
    print("No discount available for the given amount")
    print("Net payable amount: ", amount)
