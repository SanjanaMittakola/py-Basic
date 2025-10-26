#4. Power Function
#Write a recursive function to calculate a^b (a raised to the power b).

def power(p,n):
    pow=1
    for i in range (p):
        pow=pow*n
    return pow
n=int(input("Enter your number :"))
p=int(input("Enter your power :"))
print("your added number is :",power(p,n))