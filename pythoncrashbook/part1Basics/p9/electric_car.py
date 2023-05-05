##Inheritance
#When one class inherits from another it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class. The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes method of its own.

#The __init__() method for a child class

# we want to call often the __init__() method from the parent class this will initialize any attributes that were defined in the parent __init__() method an make them available in the child class.

#let's make an electric car "ElectricCar" class on the Car class we wrote earlier then well only have to write code for the attributes and behavior specific to electric cars.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):


