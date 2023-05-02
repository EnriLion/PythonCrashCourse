##Working with classes and Instances

#We can modify the attribues of an isntance directly or write methods that update attributes in specific wats.

##The Car Class

#Let's write a new class representing a car. Our class will store information abotu the kind of car we're working with , and it will have a method that summarizes information:

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
