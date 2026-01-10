#6. Factorial using Recursion
#Write a recursive function to calculate the factorial of a number.
def factorial(num):
    if(num==0 or num==1):
        return num
    else:
        return num * factorial(num-1)
        
num= int(input("Enter your number :"))
if(num>=0 or num <=9):
    print(factorial(num))
else:
    print("invelid value")
