"""
7. Train Ticket Pricing System. Input Age and travel distance (in km)
Rules:
Children (<12): ₹2/km
Adults (12–59): ₹5/km
Seniors (60+): ₹3/km
If distance > 500 km, apply 10% discount on total fare.
"""
print("Train Ticket Pricing System ")
age=int(input("Enter your age :"))
dis=int(input("Enter your tavel distance"))
if age<12:
    price=dis*2
    print("your total price is",price)
    if dis>500:
        discount=0.10*price
        price=price-discount
        print("your discount price is",price)
        
    

elif age>12 and age<59:
    price=dis*5
    print("your total price is",price)
    if dis>500:
        discount=0.10*price
        price=price-discount
        print("your discount price is",price)

elif age>59:
    price=dis*3
    print("your total price is",price)
    if dis>500:
        discount=0.10*price
        price=price-discount
        print("your discount price is",price)

else:
    print("Enter your correct age")