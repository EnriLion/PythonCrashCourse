#Passing a list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'try', 'margot']#we define a list of users and then pass the list usernames to greet_user() in our functions
greet_users(usernames)
