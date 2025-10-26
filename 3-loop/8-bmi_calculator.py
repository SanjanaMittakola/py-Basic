"""8. BMI Calculator and Health Category
Input: weight (kg) and height (m)
Calculate BMI: weight / height**2
<18.5 → Underweight
18.5–24.9 → Normal
25–29.9 → Overweight
≥30 → Obese"""
weight=int(input("Enter your weight in kg :"))
height=int(input("Enter your height in m :"))
bmi=weight / (height**2)
print("your BMI is :",bmi)
if bmi<18.5:
    print("underweight")
elif bmi >18.5 and bmi <24.9:
    print("normal")
elif bmi >25 and bmi <29.9:
    rint("overweight")
elif bmi >=30 :
    print("obese")
else:
    print("invald input")
