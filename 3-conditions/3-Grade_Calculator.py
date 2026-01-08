#Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
score = int(input("Enter your score :"))
if score >=101:
    print("Please verify your score again")
    exit()
if score >= 90:
    print("Your A grade")
elif score >= 80:
    print("Your B grade")
elif score >= 70:
    print("Your C grade")
elif score >= 60:
    print("Your D grade")
elif 60 <= score:
    print("Your F grade")
else:
    print("invalid value")



