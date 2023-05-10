#Importing multiple classes from a module

#You can import as many classes as you need If we want to import Car abd ElectricCar in the same module:

from car import Car, ElectricCar

my_bettle = Car('volkswageen', 'bettle', 2019)
print(my_bettle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#Importing an entire module
print("\n")
import car

my_bettle  = car.Car('volkswageen', 'bettle', 2019)
print(my_bettle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

##We import the full car module and then access thr classes we need through an module_name.Classname

#Importing all classes from a module

##from module_name import *

#This way is not recommended because you could be confuse  is better to import the entire module

##Now we can import from each module separately and create whatever kind of car we need:
print("\n")
from car import Car
from electric_car import ElectricCar

my_bettle = Car('volkswagen', 'beetle', 2019)
print(my_bettle.get_descriptive_name())


my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
