#Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
    
class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

class Battery:
    def battery(self):
        return "This is Battery"

class Engine:
    def engine(self):
        return "This is Engine"

class Electric(Battery, Engine, Car):  
    pass
        
mycar = Electric("Toyota", "Corolla")
print(mycar.engine())
print(mycar.battery())

