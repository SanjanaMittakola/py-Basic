#1.	Write a for loop that loops through a string and counts the number of vowels.
str=input("Enter your string :")
vlo="aeiouAEIOU"
len=0
for i in str:
    if i in vlo:
        len=len+1
print("your string have vowels is",len)