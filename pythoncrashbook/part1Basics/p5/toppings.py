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
