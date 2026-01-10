#18 pyramid pattern with borders only
#    *
#   * *
#  *   *
# *     *
#********* 
line=int(input("Enter your number to print the pattern :"))

for i in range(1,line+1):
    print(" ")
    for j in range(line-i):
        print(" ",end=" ")
    for k in range(1,i*2):
        if(i==line or k==1 or k==2*i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            

    
















