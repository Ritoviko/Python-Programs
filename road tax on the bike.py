cost = int(input("Enter the cost of the bike: Rs. "))

if cost == 100000:
    tax = (cost*15)/100
    print("Road tax: Rs ", tax)

elif cost>50000 and cost <100000:
    tax = (cost*10)/100
    print("Road tax : Rs. ", tax)

elif cost <= 50000:
    tax = (cost*5)/100
    print("Road tax: Rs. ", tax)
