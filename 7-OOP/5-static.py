#Add a static method to the Car class that returns a general description of a car.

class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    @staticmethod           
    def defination():           
        return "A car is a motor vehicle with four wheels used for transporting people safely and comfortably."

print(Car.defination())
