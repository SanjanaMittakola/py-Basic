# 16  hollow rombus pattern vrush  
#    *****
#   *   *
#  *   *
# *   *
#*****


line=int(input("Enter your number to print the pattern :"))
for i in range(0,line):
    print(" ")
    for j in range(line-i):
        print(" ",end=" ")
    for k in range(0,line):
        if i==0 or i==line-1 or k==0 or k==line-1:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
