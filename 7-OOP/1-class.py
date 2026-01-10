# Create a Car class with attributes like brand and model. Then create an instance of this class. and 
#Add a method to the Car class that displays the full name of the car (brand and model).

class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    def name(self ):
        return f"{self.brand} {self.model} "

mycar = Car("Toyota", "Corolla")
print(mycar.brand)
print(mycar.model)
print(mycar.name())