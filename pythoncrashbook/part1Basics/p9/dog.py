#Object oriented programming  is one of the most effective approaches to writing software

#You could create objects and classes

##Creating and using a class

#You can bame it almost everything using classes  writing a simple class dog and represents a dog  they have name and age  and most dpgs ait and roll over  those pieces of information(name and age) and two behaviors(sit and roll over)

#Creating the dog class

#Each instance created from the Dog class will store a name and age, and we'll give eaxh dog the ability to sit() and roll_over():

class Dog:#We define a class as dog
    """A simple attempt to model a dog"""#A docstring about the function
    def __init__(self, name, age):#A function that's part of a,class is calked a method; this is a special method that Python runs automatically whenever we create a new instance based on the Dog class. the underscores prevents the name of the other methods
        """Initialize name and age atributes"""#A docstring
        self.name = name
        self.age = age 
        #Each variables have the prefix self  every variable called like this is available to every method in the class and we'll also be accessthese variables through any instance created from the class and access through any instance
        #The line self.name = name takes the value associated with the parameter name and assigns it to the variable name,which is then attached to the instamce being created as well as the below line( this are called attributes)

    def sit(self):
        """Simulate a dog sitting in respond to a command."""#A docstring
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""#A docstring
        print(f"{self.name} rolled over.")

    #This methods only have one parameter

##Making an Instance from a Class

#Think of a class as a set of instructions fpr how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs:

my_dog = Dog('Willie', 6)#When python reads the line __init__()and its calls the init method in Dog with the arguments willie and 6.
#Python returns an instance representing this dog(that instance is representing my_dog) we can usually that a capitalize name like Dog refers to a class and a lower case name like my_dog refers to a single instance created from a class

print(f"My dog's name is {my_dog.name}.")
print(f"My dog  is {my_dog.age} years old.")

#Accesing attributes

#To access an attributes of an instance you use dot notation, we access the value of my dog attributes name by:

# my_dog.name

#Python looks at the instance my_dog and then finds the attribute name associated with my_dog  and is referred to as self.name in the class Dog

#Calling methods
print("\n")
my_dog.sit()
my_dog.roll_over()
#Creating multiple instances
print("\n")
my_dog = Dog('Willie', 6)#When python reads the line __init__()and its calls the init method in Dog with the arguments willie and 6.
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog  is {my_dog.age} years old.")
my_dog.sit()
print("\n")
print(f"My dog's name is {your_dog.name}.")
print(f"My dog  is {your_dog.age} years old.")
my_dog.sit()

#Even if contain the same data python will be consider as different instances
