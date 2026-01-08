#/* 13 hollow rectangle vush
#* * * * * 
#*       *
#*       *
#*       *
#* * * * *
line=int(input("Enter your number to print the pattern :"))
for i in range(1,line+1):
    print(" ")
    for j in range(line):
        if i==1 or i==line or j==0 or j==line-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")