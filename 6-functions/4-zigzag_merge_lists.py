#Zig-Zag Merge Two Lists alternatively: ex [1,3,5], [2,4,6] → [1,2,3,4,5,6]
def Merge(l1,l2):
    result=[]
    for i in range(max(len(l1),len(l2))):
        if i<len(l1):
            result.append(l1[i])
        if i<len(l2):
            result.append(l2[i])
    print(result)
l1 = input("Enter first list elements separated by space: ").split()
print("Your list:", l1)
l2 = input("Enter second list elements separated by space: ").split()
print("Your list:", l2)
Merge(l1,l2)
