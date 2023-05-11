#The Python Standard Library

#One interesting function is the random module is randint() and here's how to generate a random number between 1 and 6:
from random import randint, choice
print(randint(1, 6))

#from random import choice
#This function takes in a list or tuple and returns a randomly chosen element:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

