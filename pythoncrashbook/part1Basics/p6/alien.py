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

alien_0 = dict()

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#As of Python 3.7, dictionaries retain the order in which they were defined. When you print a dictionary or loop through its elements, you will see the elements in the same order in which they were added to the dictionary.

print("\n")
#Modifying values in a dictionary


alien_0 = {'color' : 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#We first define a dictionary for alien_0 that contains only the alien's color.

#The alien's current speed and then use it to determine how far to the right the alien should move:

print("\n")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}.")

# Move the alien to the right.
# Determine how far to move the alien based on its curent speed.
# For more interesting example, let's track the position of an alien that can move at different speeds. We'll store a value representing the alien's current speed and then use it to determine how far the right the alien should move:

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}.")

#Removing key-value pairs


print("\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Note: Be aware that the deleted key-value pair is removed permanently

# A dictionary of similar objects


print("\n")

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
#Note: Most editors have some functionality that helps you format extended lists and dictionaries in a similar manner to this example. Other acceptable ways to format long dictionaries are available as well, so you may see slightly different formatting in your editor, or in othe sources


