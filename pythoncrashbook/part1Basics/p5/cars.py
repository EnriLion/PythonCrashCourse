##If staments
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

##Conditional test

car = 'bmw'

variable = car == 'bmw'

print("\n",variable)


car = 'toyota'

variable = car == 'bmw'


print("\n",variable)

#if a variable is == True the code will be executed in other hand(False) won't be executed

##Ignoring case when checking for equality



car = 'Audi'

variable = car == 'audi'


print("\n",variable)

#This behavior is adavantageous but in  case doesn't matter and instead you just wan to test eh value of a variable, you can convert the variable value to lowercase before doing the comparison:


car = 'Audi'

variable = car.lower() == 'audi' #you can do this kind of comparison without the value that was originally stored in car.


print("\n",variable)


