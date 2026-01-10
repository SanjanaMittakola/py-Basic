#3. Sum of Digits
#Write a recursive function to calculate the sum of the digits of a number.

def digit(num):
    add=0
    total=0
    while num!=0:
        add=(num%10)
        num=num//10
        total=total+add
    return total
num=int(input("Enter your number :"))
print("your added number is :",digit(num))