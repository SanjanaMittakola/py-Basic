#Keep asking the user for input until they enter a number between 1 to 10
while True:
    n=int(input("Enter value between 1 to 10 : "))
    if 1 <= n <= 10:
        print("Okk")
        break
    else:
        print("invalid value, try again")