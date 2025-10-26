 #	         *
 #	       *   *
 #	     *   *   *
 #	   *   *   *   *
 #	 *   *   *   *   *      
line=int(input("Enter your number to print the pattern :"))
for i in range(1,line+1):
    print(" ")
    for j in range(line-i):
        print(" ",end=" ")
    for k in range(i):
        print(" * ",end=" ")