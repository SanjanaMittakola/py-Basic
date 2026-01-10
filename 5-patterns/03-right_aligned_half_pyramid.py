# * * * * * *
#   * * * * *
#     * * * *
#       * * * 
#         * * 
#           * 

line=int(input("Enter your number to print the pattern :"))
for i in range(0,line):
    print("")
    for j in range(i):
        print(" ",end=" ")
    for k in range(line-i):
        print("*",end=" ")