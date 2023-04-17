#Passing arguments
##We can use positional arguments which needto be in the same order were written as keyword argument(each argument consists of a variable name and a valur (list and dictionaries of values)

#Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\n I have a {animal_type}")
    print(f"\n My {animal_type}'s name is {pet_name}")

describe_pet('hamster','harry')

#When we call describe_pet  we need to provide and animal type and namein that order
#The function call the argument hamster is assigned to the parameter animal_type as well as harry 

#Multiple function calls

describe_pet('dog','willie')

#Order matters in position arguments

describe_pet('while','dog')

#Keyword arguments


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#Note:When you use keyword arguments, be sure to use the exact names of the parameters in the function's definition.

#Default values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about pet"""
    print(f"\n I have a {animal_type}")
    print(f"\n My {animal_type}'s name is {pet_name}")

describe_pet(pet_name='willie')



