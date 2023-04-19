##Returning a simple value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"# the function combines thse two names, adds a space between them, and assigns the result to  full_name
    return full_name.title() #the value of full_name is converted to title case, and then returned to the calling line 

musician = get_formatted_name('jimi', 'hendrix') #the assigned value is assigned to the variable musician and the output shows a neatly formatted name made up of the parts of a person's name.
print(musician)

#The function make the same as simple as printing it

print("Jimi Hendrix")

##Making an argumental optional

#Only using default values we could make an argument optional
print("\n")

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hooker')
print(musician)

#we could choose if we want to make the middle name optional, we can give the middle_name argument an empty default value and ignore the agument unless the user provides a value.
print("\n")

def get_formatted_name(first_name, last_name, middle_name=''):# the middle_name is optional that is why there are not string only a '' empty string
    """Return a full name, neatly formatted."""#python interprets middle_name as  a true or false like a flag
    if middle_name:
         full_name = f"{first_name} {middle_name} {last_name}"
    else:
         full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)

# Optional values allow functions to handle a wide range of use cases whiel letting function calls remain as simple as possible



