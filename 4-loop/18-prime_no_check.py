#Check if number is prime.
n= int(input("Enter your value :"))
if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("Number not a prime number")
            break
        else:
            print("Number is a prime number")
            break