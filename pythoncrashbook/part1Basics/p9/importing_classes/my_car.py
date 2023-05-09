# the import statement tells Python to open the car module and import the class Car. Now we can use the Car clas as if it were defined in this file
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Importing the classes is a lean way to program we could still get the same fucntionality, but we keep your main program file clean and easy to read. You also store most of the logic in separate files. we can leave those files alone and focus on the higher-level logic of your main program.
