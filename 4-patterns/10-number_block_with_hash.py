 # 1
 # 2 3
 # 4 5 6
 # 7 8 9 10 
 # 11 12 13 14 15*/


line=int(input("Enter your number to print the pattern :"))
n=1
for i in range(1,line+1):
    print(" ")
    for j in range(i):
        print(n,end=" ")
        n=n+1