#17 pal in dromic pattern with number pattern vrush
#    1
#   212
#  32123
# 4321234
#543212345
line=int(input("Enter your number to print the pattern :"))
for i in range (1,line+1):
    print("  "*(line-i),end=" ")
    for k in range(i,1,-1):
        print(k,end=" ")
    for m in range(i):
        print(m+1,end=" ")
    print(" ")