#Passing an arbitrary numbers of arguments

# def make_pizza(*toppings):
def make_pizza(size, *toppings):
    # """Print the list of toppings that have been requested."""
    # print(toppings)
    #we can replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered:
#Mixing positional and arbitrary arguments
    """ Summarize the pizza we are about to make."""
    # print("\nMaking a pizza with the following toppings:")
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

# Note:Youll often see the generic parameter name *args, which collects arbitrary positional arguments like this.

##Storing your functions in modules

#We could use a descriptive names for our finctions and will be easier to follow but there are functions in a separate file called a "module" and "importing" that module into your main program.

#An import statement tells Python to make the code in a module available in the currently running program file.

#Knowing how to import functions also allows you to use libraries of functions that ohter programmers have written. There are several ways to import a module,and I'l show you each of these briefly.

#Importing an entire module

#The first is to create a module( is a file ending in.py)... lets make a module that contains the function make_pizza(). to make this module, well remove everything from the pizza.py except the function make_pizza():

#def make.... (its above)
