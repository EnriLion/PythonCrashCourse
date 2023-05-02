##Working with classes and Instances

#We can modify the attribues of an isntance directly or write methods that update attributes in specific wats.

##The Car Class

#Let's write a new class representing a car. Our class will store information abotu the kind of car we're working with , and it will have a method that summarizes information:

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):# we gave three parametes the make, model and year for our instance
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        ##Setting a defualt value for an attribute
        #When an instance is created, attributes can be defined without being passed in as parameters these could defined in the init where there are assigned a default value(lets add an odometer) 
        self.odometer_reading= 0 #creating a new attribute called odometer and sets the intialize value to 0

    def read_odometer(self):# we have a method that takes easy to read a car's mileage.
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):# this method takes ina mileage value and assigns it to self.odometer_reading
        """Set  the odometer reading to the given value."""
        self.odometer_reading = mileage

        #We can extend the method update_odometer() to do additional work every time the odometer reading is modified. Let's add a little logic to make sure no one tries to roll back the odometer reading:

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:# if the new mileage is greater than or euql to the existing mileage, self.odomoter_reading, you can update the odomter reading to the new mileage.
            self.odometer_reading = mileage
        else:
            print("You can't roll back and odometer!") #elsse is less than the existing mileage you'll get a waning that you can't roll back an odometer



    def get_descriptive_name(self):#we define a method called get_descriptive_name() that puts a car's year,make and model into one string nealty describing the car
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    ##2)Modifying an attribute's value through a method
    #It can be helpful to have mthods that update certain attributes for you. Instrad of accessing the attribute directly, you pass the new value to a method that handles the updating internally:

    ##3)Incrementing an Attribute's Value throguh a method.
    #Sometimes you'll want to increment  an attribute's value by a certain amount reather than a set an entirely new value(Say we buy a used car and put 100 miles on it between the time we buy it and the time we registered it)

    def increment_odometer(self, miles):#Takes in a
        """Add the fiven amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi','a4',2019)#we make an instance from the Car class and assing it to the variable 
print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

##Modifying attribute values

#1)You can change the value directly through an instance
#2)Set the value through a method
#3)Increment the value through a method or increment the value

#1)Modifying an attribute's value directly
#The simplest way to modify the value of an attribute is to access the attribute directly through an instance, readinf the odometer(23) directly:
my_new_car.odometer_reading = 24
my_new_car.read_odometer()

#2)We call update_odometer() and give it 23 ar argument(corresponding to the mileage parameter in the method definition). Its sets the odometer reading to  23 and read_odometer()
my_new_car.update_odometer(25) #we call update_domoter() and fi
my_new_car.read_odometer()

print("\n")
#3)
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



