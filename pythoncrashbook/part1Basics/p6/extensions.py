Fish = {'race': 'tuna', 'owner': 'diego'}
Cat = {'race': 'abyssinian', 'owner': 'henry'}
Dog= {'race': 'american', 'owner': 'leo'}

Pets = [fish, cat, dog]

for Pet in Pets:
    print("Every pet we could care of ", Pet)

# A list in a dictionary

#Store information about a pizza being ordered.

Pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }

#Summarize the order

print(f"\tYou ordered a {pizza['crust']} crust pizza with the following toppings:")

for Topping in Pizza['toppings']: #We  write for loop to acces the list of toppings, we use the key 'toppings' and Python grabs the list of toppings from the dictionary
    print("\t" + topping)
