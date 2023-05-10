#Importing a module into a module

##For  example let's store  the Car class in one module and the ElectricCar
#and Battery classes in a separated module. We'll make a new module called electric_car.py replacing the electric_car.py file we created earlier - and copy just the Battery and ElectricCar classes into this file:

"""A set of classes that can be used to represent electric cars."""
from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print a statement abut the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """
       super().__init__(make, model, year) 
       self.battery = Battery()
#The class ElectricCar needs access to its parent class Car, so we import Car directly into the module at 1 if we forget this line, Python will raise an error when we try to import the electric_car module. We also need to update the Car module so it contains only the Car class:


#car module(car.py)

#"""A class that can be used to represent a car."""

#class Car:
# --snip--
