# A list in a dictionary

#Store information about a pizza being ordered.

pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }

#Summarize the order

print(f"You ordered a {pizza['crust']} crust pizza with the following toppings:")

for topping in pizza['toppings']: #We  write for loop to acces the list of toppings, we use the key 'toppings' and Python grabs the list of toppings from the dictionary
    print("\t" + topping)
