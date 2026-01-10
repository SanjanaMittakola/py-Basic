#.  Find All Prime Numbers Between Two Limits Using Function
def prime(n1,n2):    
    for i in range (n1,n2+1):
        if i>1:
            for j in range (2,int(i**0.5)+1):
                if i % j ==0:
                    break
            else:
                print(i) 

n1=int(input("Enter your starting number : "))
n2=int(input("Enter your ending number : "))
prime(n1,n2)