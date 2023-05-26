#This program imports the get_formatted_name() from name_function.py  The user can enter a series of first and last names, and see the fromatted full names that are generated:

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

#We can see the names generated correct if we want to modify get_formatted_name() and can also handle middle names. As we do so, we want to make sure we don't break the way the function handles names that have only a first and last name and we could test our code by running this file but this is tedious that why python provides a wat to automate the testing of a function's output if we automate the testiong get_formatted_name we can always be confident that the function will work when given the kind of names.
