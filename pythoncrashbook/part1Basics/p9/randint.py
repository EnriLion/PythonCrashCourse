#The Python Standard Library

#One interesting function is the random module is randint() and here's how to generate a random number between 1 and 6:
from random import randint, choice
print(randint(1, 6))

#from random import choice
#This function takes in a list or tuple and returns a randomly chosen element:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

#The random module shouldn't be used when building security-related applications, but it's good enough for many fun and interesting projects

#Note: You can also download modules from external sources. You'll see a number of these examples in Part II, where we'll need external modules to complete each model
