#performing the operations using tuple
fruit=("mango","apple","orange","banana","pineapple","graph")
n=(3,5,7,8)
#nesting
print("your tuple of fruit and n is :",fruit,n)
#repiting
rep=("python ")*5
print("your repiting value is :",rep)
#slicing
print("your slicing values is :",n[1:])
#unpacking
ch=tuple("hlloiamhere")
print("your string converted into ch",ch)
a,*b,c=n
print("your n is assinging value into character a,b,c :",a,b,c)
