##Checking for Inequality

# != -> not

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Gold the anchovies!")

#the if stament to examine how to use the inequality operator. We'll store a requested pizza topping in a vaiable and then printing a message int eh person did not order anchovies as the example above

##Numerical Comparisons

#Testing numerical values is pretty strighforward

Age = 18

Under_age = Age == 18

print("\n",Under_age)

#Testing multiple conditions

#using when we want that only going to be true if in case is True

requested_topping = ['mushrooms', 'extracheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping: 
    print('Adding pepperoni.')
if 'extracheese' in requested_topping:
    print('Adding extra cheese.')

print("\nFinished making you pizza!")

#This code doesn't work in an if-else block:


requested_topping = ['mushrooms', 'extracheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_topping: 
    print('Adding pepperoni.')
elif 'extracheese' in requested_topping:
    print('Adding extra cheese.')

print("\nFinished making you pizza!")

#the block sentence will never work because the extracheese or pepperoni are never checked and all the first will be added but all their other toppings will be missed.


##Checking for special items


print("\n")

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

#Runs out of green pepper

print("\n")

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
         print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")


print("\n")

#Checking that a list ia not empty

requested_toppings = list()

if requested_toppings:  
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print("\n")

#Using multiple lists

available_toopings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese' ]

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toopings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we dont have  {requested_topping}")

print("\nFinished making your pizza!")

print("\n")


