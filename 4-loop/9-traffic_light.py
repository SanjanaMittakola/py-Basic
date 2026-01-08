"""16. Traffic Light Simulation
Input: Light color ("Red", "Green", "Yellow")
Output:
Red → "Stop"
Green → "Go"
Yellow → "Wait"
Any other → "Invalid light color"
"""
light=input("Enter light color :")
if light=="red" :
    print("stop")
elif light=="green" :
    print("go")
elif  light=="yellow" :
    print("wait")
else:
    print("Invalid light color")