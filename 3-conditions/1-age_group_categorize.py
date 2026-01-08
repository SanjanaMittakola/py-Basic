#Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age= int(input("Enter your age :"))
if age < 13:
    print("child")
elif age <= 19:
    print("Teenager")
elif  age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")
else:
    print("invalid value")

