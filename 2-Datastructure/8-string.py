#strings all opertaion are perform

str="python learning"
str1="SDFGHJ"
print(" string is :",str)
print(" string index value from 0 to 6 :",str[0:6])
print(" string index value from : 5 :",str[:6])
print(" string index value from 5 to end :",str[6:])
print(" string from 3 to 8 :",str[3:8])
print(" value convert lower into upper case :",str.upper())
print(" value convert upper into lower case :",str1.lower())
print(" string find l :",str.find('l'))
print(" string index l :",str.index('l'))
print(" string split :",str.split(" "))
print("string replace: ",str.replace("python","hii python"))
print("string rpartition is :",str.rpartition(" hii "))
con=str + " " + str1
print("concation of str and str1 :",con)
str3="{},{}".format(str,str1)
print("changing format :",str3)