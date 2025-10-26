#converting list to tuple 
list=[1,2,3,4,5,6]
print("type of a data is:",type(list))
tpl=tuple(list)
print("converted list into tuple : ",tpl)
print("type of a data is:",type(tpl))

#nesting tuple in a list
list=[(1,2,3),(5,6,7)]
print("list is :",list)
list.append(("apple","orange","banana"))
print("append list is: ",list)
list.remove((1,2,3)) 
print("removing list data is :",list)

#nesting list in a tuple
tpl=(['a','b','c'],['f','e','t'])
print("tuple is :",tpl)
tpl[0].append('o')
print("append tuple is :",tpl)