#dictionaries creating and accessing and deleting
d1={}
print("empty dic :",d1)
print("type :",type(d1))
d2={1:"mango",2:"apple",3:"orange",4:"pine apple",5:"banana",6:"graphs"}
print("dictionary is :",d2)
d3=dict([(1,"dog"),(2,"cat"),(3,"lion"),(4,"tiger"),(5,"donkey"),(6,"mouse")])
print("dictionary is :",d3)
d4={"bird":{1:"peocok",2:"parrat",3:"crow"},"age":34}
print("dictionary iner dictionary is:",d4)
d2[6]="sanjan"
for key, value in d2.items():
    print(key, value)
#or 
for dd in d2:
    print(dd, d2[dd])
print("Adding element : ",d2)
print("accessing value :",d2.get(6))
print("deleting value of d2 index 7 :",d2.pop(6))
print("deleting all value of dic :",d4.popitem)
item = {
    "Fruits": {"First": "Apple","Second": "Orange","Third": "Pineapple","Fourth": "Mango","Fifth": "Banana"},
    "Vegetables": {"First": "Onion","Second": "Potato","Third": "Tomato","Fourth": "Cauliflower","Fifth": "Carrot"},
    "Animals": {"First": "Cat","Second": "Dog","Third": "Rat","Fourth": "Tiger","Fifth": "Lion"}
}
print(item)
print(item["Fruits"])
print(item["Animals"]["Fifth"])
