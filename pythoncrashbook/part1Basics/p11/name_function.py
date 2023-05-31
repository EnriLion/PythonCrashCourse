#Testing a function

#To learn about testing, we need code to test. Here's a simple function that takes in a first and last name and returns a neatly formatted full name:

# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()
#get_formatted_name() combines the first and last name to check we will make a program that uses this function(names.py) lets users enter a first and last anme, and see neatly formatted full name.

#A Failing Test

# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

#Responding a failed test

#In this case  the function brokes because the three parameters to modify thecode we could modify it and make the parameter optional

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
