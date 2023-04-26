#Using arbitrary keyword arguments

#We could write functions that accept as many key-value pairs as the calling statement provides.One example involves building user profiles: you know you'll get information about a user, but you're not sure what kind of information you'll receive
#the function below in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:
def build_profile(first, last, **user_info):#in the body we add the first and last names to the user_info because we'll always receive these two pieces of information from the user and they haven't been placed into the dictionary yet
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last 
    return user_info

user_profile = build_profile('leon', 'enrique', hobby='reading', expertise='linux', job='developer')

print(user_profile)

#you can mix positional, keyword and arbitrary values in may diferent ways when writing your own functions and is useful to know that all these arguments types exist because you'll see them often when you start reading other people's code.

#note: you'll often see the parameter name **kwargs used to collect non-specific keyword arguments

