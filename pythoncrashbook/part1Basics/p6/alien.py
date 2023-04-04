##A Simple Dictionary

#Consider a game featuring aliens that can have different colors and point values. This simple dictionary stores information about a particular alien:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Working with Dictionaries

#A dictionary in Python is a collection of a key_value pairs. Each key is connected to a value(a tring, number, list or even another dictionary)

#The dictionaries are wrapped in braces, { } with a series of key valu in pairs inside the braces, as shown in the earlier example:


alien_0 = {'color': 'green'}

print("\n")
#Accessing Values in Dictionary


print(alien_0['color'])


alien_0 = {'color': 'green', 'points': 5}

#Using either color or the point value of alien_0. I fa player shoots down this alien, you can look up how many points they should earn using code like this:

new_points = alien_0['points']

print(f"You just earned {new_points} points!")


print("\n")

#Adding New Key-Value Pairs

print(alien_0)

print("\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#As of Python 3.7, dictionaries retain the order in which they were defined. When you print a dictionary or loop through its elements, you will see the elements in the same order in which they were added to the dictionary.

#Starting with an Empty Dictionary

alien_0 = list()

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#As of Python 3.7, dictionaries retain the order in which they were defined. When you print a dictionary or loop through its elements, you will see the elements in the same order in which they were added to the dictionary.

#Starting with an Empty Dictionary

alien_0 = list()


