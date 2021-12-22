item = int(input("Enter the total items you have purchased = "))
total = 0
for i in range(1, item+1):
    print("Enter the cost of", i, "item: ")
    cost = int(input())
    total = total+cost

if total>=8000:
    dis = (total*30)/100
    total = total-dis
    print("You have to pay total of Rs. ", total)
else:
    print("You have to pay total of Rs. ", total)
