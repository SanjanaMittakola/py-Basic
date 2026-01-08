#Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
fruit = "Banana"
color = input("Enter your fruit color : ")
if fruit == "Banana":
    if color == "green":
        print(fruit,"is Unripe")
    elif color == "yellow":
        print(fruit,"is ripe")
    elif color == "Brown":
        print(fruit,"is Overripe")
    else:
        print("Invalue value")