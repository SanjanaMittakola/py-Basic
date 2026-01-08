#1 2 3 4 5 
#1 2 3 4
#1 2 3 
#1 2
#1 
line=int(input("Enter your number to print the pattern :"))
for i in range(0,line):
    print(" ")
    for j in range(line-i):
        print(j+1,end=" ")
