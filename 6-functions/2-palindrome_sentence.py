#Palindrome Sentence Checker (Ignore Spaces, Case)
def palindrome(str):
    str1=""
    le=len(str)-1
    for i in range(le,-1,-1): 
        str1=str1+str[i]
    return str1
str=input("Enter your string :")    
palindrome(str)
if(palindrome(str)==str):
    print("It's a palindrome.")
else:
    print("Not a palindrome.")
