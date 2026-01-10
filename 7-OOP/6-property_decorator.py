#Use a property decorator in the Car class to make the model attribute read-only

class Car:      
    def __init__(self, brand, model): 
        self.brand = brand
        self.__model = model

    @property           #@property decorator is used to access a class method like an attribute without calling it as a function. 
    def model(self):           
        return self.__model
    

mycar = Car("Toyota", "Corolla")

print(mycar.model)