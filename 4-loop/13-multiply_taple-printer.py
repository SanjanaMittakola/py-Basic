#print the Multiplication table for a given number up to 10, but skip the fifth iteration

num=int(input("Enter your value: "))
for i in range(1,11):
    if i != 5:
        mul=num*i
        print(num,"x",i, "=",mul)
#or
    #if i==5:
        #continue
    #mul=num*i
    #print(num,"x",i, "=",mul)
