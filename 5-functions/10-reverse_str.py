#Write a recursive function to reverse a string.


def reverse_str(str):
    str1=""
    length=len(str)-1
    for i in range(length,-1,-1):
        str1=str1+str[i]
    return str1
    
str=input("Enetr your string : ")
print(reverse_str(str))