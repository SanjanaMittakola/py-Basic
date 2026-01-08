#5. You are given a list of numbers. Write a loop that finds the second largest number without using max() or sorting.
lst=[2,3,4,5,63,983]
if len(lst) < 2:
    print("list atleat two numbers")
else:        
    if lst[0] > lst[1]:
        lar1=lst[0]
        lar2=lst[1]    
    else:
        lar1=lst[1]
        lar2=lst[0]

for i in range(2, len(lst)):
    if lst[i] > lar1:
        lar2=lar1
        lar1=lst[i]
    elif lar[i]>lar2 and lst[i]!=lar1:
        lar2=lar[i]
print("your second largest number is :",lar2)
