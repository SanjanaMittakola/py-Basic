#Demonstrate the use of isinstance() to check if mycar is an instance of Car and ElectricCar.

class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    
class Electric(Car):        
    def __init__(self, brand, model, battery): 
        super().__init__(brand, model)      
        self.battery = battery
        
mycar = Electric("Toyota", "Corolla", "90kwh")

print(isinstance(mycar,Car))
print(isinstance(mycar,Electric))
