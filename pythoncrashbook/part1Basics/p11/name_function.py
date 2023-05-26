#Testing a function

#To learn about testing, we need code to test. Here's a simple function that takes in a first and last name and returns a neatly formatted full name:

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
#get_formatted_name() combines the first and last name to check we will make a program that uses this function(names.py) lets users enter a first and last anme, and see neatly formatted full name.

