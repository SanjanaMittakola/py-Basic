#Calculate the sum of even number up to a given number n.
n=int(input("Enter your value: "))
sum=0
for i in range(1, n+1 ):
    if i%2 == 0:
        sum=sum+i

print("sum of all even values :",sum)