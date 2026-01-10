#Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:      
    def __init__(self, brand, model): 
        self.__brand = brand        #__ is use as  private
        self.model = model

    def get_brand(self, brand):         #encapsulation get_variable name to hide variable
        return self.__brand
    def name(self ):
        return f"{self.__brand} {self.model} "      #f is format

mycar = Car("Toyota", "Corolla")
print(mycar.get_brand)
print(mycar.model)
print(mycar.name())