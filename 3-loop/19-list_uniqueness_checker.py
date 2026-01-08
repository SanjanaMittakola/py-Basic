#check if all element in a list are unique. if a dublicate is found, exit the loop and print the dublicate
item=["Apple","Banana","Orange","Apple","Mango"]
unique = set()
for ch in item:
    if ch in unique:
        print("Dublicate value is ",ch)
        break
    unique.add(ch)
