#Given  a string, find the first non-repeated character
str=input("Enter your string :")
for ch in str:
    if str.count(ch) == 1:
        print("First non-repeated character :",ch)
        break
