#1.	Check Perfect Number Using Function A number is perfect if sum of its proper divisors equals the number itself.
#Example: 28 → 1 + 3  + 7 + 14 = 28 ✅
def number(n):
    sum=0
    if n<=0:
        return false
    for i in range(1,n):
        if n % i ==0:
            sum=sum+i
    return sum==n
n=int(input("Enter your number :"))
if number(n):

    print("perfect")
else:
    print("not perfect")