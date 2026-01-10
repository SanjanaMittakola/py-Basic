#Create a function that returns both the area and circumference of a circle given its radius
 
import math

def circle(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area , circum

a, c = circle(5)
print("area of circle",a,"\ncircumference of circle :",c)