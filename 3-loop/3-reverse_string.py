#3. Write a loop to reverse a string without using slicing ([::-1]).
str=input("Enter your string :")
str1=""
l=len(str)-1
while l>=0:
    str1=str1+str[l]
    l=l-1
print(str1)
