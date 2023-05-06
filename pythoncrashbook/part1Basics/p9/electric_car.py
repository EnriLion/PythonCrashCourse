#The __init__() method for a child class

#you;ll often call __init__() method from the parent class. this will initialize any attributes that were defined in the parent __init__() method and make them available in the child class
#As an example we are going to create a ElectricCar class on the Car class we wrote earlier.Then we'll only have to write code for the attribytes and behavior specific to electric cars.

class Car:#parent class of the electric_car
    """A simple attempt to represent a car."""

    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odomter_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment(self, miles):
        self.odometer_reading += miles

#Instances as attributes

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")



class ElectricCar(Car):#we define the child class ElectricCar  and the name of the parent clas must be included in the parentheses
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):# the init_method takes the information required to make a Car instance
        # """Initialize attributes of the parent class."""
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """
       super().__init__(make, model, year)#Is a special function that allows to call a method from the parent class this line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all tha attributes defined in that method. Super comes from a convention of calling the parent class a superclass and the child class a subclass
       self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    #Overriding Method from the Parent Class

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gast tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

##Defining attributes and methods for the child class

#Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.

#let's add an attribute that's specific to electric cars ( battery,etc) and a method to report on this attribute( we store the battery size and write a method that prints a description of the battery):

#There's no limit to how much you can specialize the ElectricCar class. You can add as many attributes and methods as you need to model an electric car to wathever degree of accuracy you need. An attribute or method that could belong to any car, rahter than one that's specific to an electric car, should be added to the Car class instead of the ElectricCar calss. Then anyone who uses the Car class will have that functionality available as well and the Electri Car class will only contain code for the information and behavior specific to electric vehicles.

##Overriding methods form the parent class

#Python will disregard the parent class method and only pay attention to the method you define in the child class.

#Say the class Car had a method called fill_gas_tank(). This method is meaningless for an an all-electric vehicle, so you might want to override this method. Here's one wat to do that:

#If someone ties to call fill_gas_tank() with an electri car, Python will ignore the method in Car and run this code instead. When you use inheritance, you can make your child classes retain what you need and override anything you don't need from the parent class.

##Instances as attributes

