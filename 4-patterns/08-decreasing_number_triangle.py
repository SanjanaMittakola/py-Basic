 # 5
 # 4 4
 # 3 3 3
 # 2 2 2 2
 # 1 1 1 1 1
line=int(input("Enter your number to print the pattern :"))

for i in range(0,line):
    print(" ")
    for j in range(i+1):
       print(line-i,end=" ")