 # 1
 # 1 2
 # 1 2 3
 # 1 2 3 4
 # 1 2 3 4 5
line=int(input("Enter your number to print the pattern :"))
for i in range(1,line+1):
    print(" ")
    for j in range(i):
        print(j+1,end=" ")