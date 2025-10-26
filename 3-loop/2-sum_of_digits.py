#Find the sum of all digits in a number using a while loop.
num=int(input("Enter of element : "))
n=0
while num>0:
    digit=num%10
    n=n+digit
    num=num//10
print("additon of element is :",n)