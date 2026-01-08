#Reverse a string using loop
str=input("Enter your string : ")
rev=""
for ch in str:
    rev=ch+rev
print("Reverse a string is :",rev)