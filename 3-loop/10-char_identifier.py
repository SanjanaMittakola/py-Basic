"""
10. Character Identifier
Input: a single character
If it's a vowel → "Vowel"
If consonant → "Consonant"
If digit → "Digit"
If symbol → "Special character"""
ch=input("Enter character :")
if(ch>="a" and ch<="z"):
    if(ch in ['a', 'e', 'i', 'o', 'u']):
        print("your enterd a vowel")
    else:
        print("your enterd a consonant")
elif(ch>="0" and ch<="9"):
    print("your enterd a digit")
else:
    print("your enterd a special character")