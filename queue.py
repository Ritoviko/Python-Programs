arr = []
def enqueue(arr, x):
    arr.append(x)

def dequeue(arr):
    if len(arr)>0:
        arr.pop(0)
    else:
        print("Underflow")
        print("-+-+-+-+-+-+-+-+-+-+-+-")

def display(arr):
    if len(arr)>0:
        for i in range(len(arr)):
            print(arr[i])
    else:
        print("Underflow")
        print("-+-+-+-+-+-+-+-+-+-+-+-")


while True:
    print("Enter your option: ")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    print("-+-+-+-+-+-+-+-+-+-+-+-")
    opt = int(input("Enter your choice: "))
    print("-----------------------")
    if opt == 1:
        x = int(input("Enter the element: "))
        print("-----------------------")
        enqueue(arr, x)
    elif opt == 2:
        dequeue(arr)
    elif opt == 3:
        print("The Queue elements are: ")
        display(arr)
        print("-----------------------")
    elif opt == 4:
        print("Bye")
        break
    else:
        print("Wrong input")
        print("-----------------------")
