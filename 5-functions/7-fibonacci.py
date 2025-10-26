#Fibonacci Sequence using Recursion
#Write a recursive function to return the n-th number in the Fibonacci sequence.
#📥 Input: 7
#📤 Output: 8 (sequence: 0, 1, 1, 2, 3, 5, 8)
def fibo(i):
    if(i<=1):
        return i
    else:
        return fibo(i-1) + fibo(i-2)

num=int(input("enter your number :"))
for i in range(num):
    print( fibo(i), end=" ")
    
