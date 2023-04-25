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

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

# Note:Youll often see the generic parameter name *args, which collects arbitrary positional arguments like this.

