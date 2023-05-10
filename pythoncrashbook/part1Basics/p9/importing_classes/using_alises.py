#Using Alises

#We could use alises when importing classes as well for exmple if we eant to import the ElectricCar in alias in the import statement:
from electric_car import ElectricCar as EC
#Now you can use this alias whenever you want to make an electric car:
my_tesla = EC('tesla', 'roadster', 2019)
