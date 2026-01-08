#Compute the Factorial of a number using while loop
n=int(input("Enter your number : "))
factorial=1
while n>=1:
    factorial=factorial*n
    n=n-1
print("Factorial of a ",n," : ",factorial)
