#Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model
    
    def fuel(self):                 #polymorphism 2 class having same function name but returning diff values
        return "Diesel or Petrol"

class Electric(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
            
    def fuel(self):                 #polymorphism 
        return "Electric car"
        
        
mycar1 = Electric("Toyota", "Corolla", "90kwh")
mycar2 = Car("Tesla", "model S")
print(mycar1.fuel())
print(mycar2.fuel())


