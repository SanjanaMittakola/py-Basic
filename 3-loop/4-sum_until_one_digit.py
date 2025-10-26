#Sum of Digits Until One Digit
#Input a number, repeatedly sum its digits until a single digit remains.
#Example: 987 → 9+8+7=24 → 2+4=6

num=int(input("Enter of element : "))
while num>10:
    n=0
    while num>0:
        digit=num%10
        n=n+digit
        num=num//10
    num=n
print("additon of element is :",n)


