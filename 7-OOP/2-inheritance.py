#Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    def name(self ):
        return f"{self.brand} {self.model} "

class Electric(Car):        #inherited class
    def __init__(self, brand, model, battery): 
        super().__init__(brand, model)      #function accessing variable
        self.battery = battery
        
mycar = Electric("Toyota", "Corolla", "90kwh")
print(mycar.brand)
print(mycar.model)
print(mycar.battery)
print(mycar.name())