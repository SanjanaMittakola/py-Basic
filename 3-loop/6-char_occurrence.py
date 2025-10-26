#6. Count Occurrence of Each Character in a String
#Input a string and count how many times each character occurs using loops (no Counter or dicts)
str=input("Enter your string :")
lst=[]
for i in range (len(str)):
    count=0
    if str[i] not in lst:
        for j in range(len(str)):
            if str[i]==str[j]:
                count=count+1
        lst.append(str[i])
        print(str[i],"occur",count,"time in your string")
