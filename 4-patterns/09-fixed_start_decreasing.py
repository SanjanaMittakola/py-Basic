 # 5
 # 5 4
 # 5 4 3
 # 5 4 3 2
 # 5 4 3 2 1
line=int(input("Enter your number to print the pattern :"))
for i in range(0,line):
    print(" ")
    for j in range(i+1):
        print(line-j,end=" ")