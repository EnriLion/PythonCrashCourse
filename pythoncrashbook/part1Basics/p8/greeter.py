import greeter_functions 
from greeter_functions import greet_user
from greeter_functions import greet_user as g
import greeter_functions as gr
from greeter_functions import *
#Defining a function

# def greet_user():
#     """Display a simple greetimg.""" #this is called a docstring, whcih describe what the function does( are enclosed in triple quotes)
#     print("Hello!")

# greet_user()#the function only has one job print("Hello")

#Passing information to a function
print("\n")

# def greet_user(username):
#     """Display a simple greetimg.""" #this is called a docstring, whcih describe what the function does( are enclosed in triple quotes)
#     print(f"Hello, {username.title()}!")

greeter_functions.greet_user('jesse')#the function has the job to passing the username to a function
print("\n")
greet_user('jonathan')
print("\n")
g('andrade')
print("\n")
gr.greet_user('michael')

#Arguments and Parameters

#The variable username in the definition of greet_user() is an example of a "parameter" a piece of information that's passed from a function call to a function

#In this case the argument 'jesse' was passed to the function greet_user(), and the value was assgined to the parameter username

#Note: People sometimes speak of arguments and parameters interchangeably. Don't be surprised if you se the variable sin a function definition referred to as arguments or the variables in a function call referred to as paraimeters.
print("\n")

##Using a function with a while loop

##gretting people with the get_formatted_name() function with a while loop to greet users more fomrally:
# def get_formatted_name(first_name, last_name):
#     """Return a full name neatly formatted."""
#     full_name =f"{first_name} {last_name}"
#     return full_name.title()

##This is an infinite loop!
#while True:
#    print("\nPlease tell me your name:") # the while loop as the user to enter their name and we prompt the name separately
#    f_name = input("First name: ")
#    l_name = input("Last name: ")

#    formatted_name = get_formatted_name(f_name,l_name)
#    print(f"\nHello, {formatted_name}!")

#The problem with this example is that we haven't defined a quit conditiont and is easlity with the break statement

print("\n")


# def get_formatted_name(first_name, last_name):
#     """Return a full name neatly formatted."""
#     full_name =f"{first_name} {last_name}"
#     return full_name.title()
v = input('You want to enter to this loop(y or yes)')
if v == 'y' or v == 'yes':
    while True:
        print("\nPlease tell me your name")   
        print("(enter 'q' at any time to quit)")
        f_name = input('First name: ')
        if f_name == 'q':
            break
        l_name = input('Last name: ')
        if l_name == 'q':
            break
        formatted_name = get_formatted_name(f_name,l_name)
        print(f"\nHello, {formatted_name}!")
else:
    print('Ok')
