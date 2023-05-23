#Saving and reading user-generated data
#Where we primpt the user for their name the first time they run a program and then remember their name when they run the program again.
import json

# username = input("What is your name? ")#we prompt for a username to store


#filename = 'username.json'

## with open(filename, 'w') as f:
##     json.dump(username, f)# passing it a username and a file object to store the username
##     print(f"We'll remember you when you come back, {username}!")#We print the message informing

##We are going to modify our program to recognize the string(user)
#try:
#    with open(filename) as f: #we try to open the file username if the file exist we read the usernam back into the memory
#        username = json.load(f)#print a message welcoming back the user int eh else block
#except FileNotFoundError:#where we prompt the user to enter the user name
#    username = input("What is your name?")
#    with open(filename, 'w') as f:
#        json.dump(username, f)#we use json.dump to store the user name and print greeting
#        print(f"We'll remember you when you come back, {username}!")
#else:
#    print(f"Welcome back, {username}!")

#Refactoring

#Refactoring is improve the code by breaking up into a series of functions that have specific jobs.(Makes your code cleaner, easier to understand and easier to extend)

def get_stored_username():
    """Greet the user by name."""#this function retrieves a stored username and returns the username
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None#if the file username.json doesn't exist the function returns None
    else:#This is a good practice: a function should either return the value you're expecting or it should return None
        return username

#We should factor one more and is the get_new_username():
def greet_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)

def greet_user():
    """Greet the user by name."""#a docstring about how currently works
    # filename = 'username.json'
    # try:
    #     with open(filename) as f:
    #         username = json.load(f)
    # except FileNotFoundError:
    #     username = input("What is your name? ")
    #     with open(filename, 'w') as f:
    #         json.dump(username, f)
    #         print(f"We'll remember you when you come back, {username}!")
    # else:
    #     print(f"Welcome back, {username}!")
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")#we print a welcome back message to the user if the atttempt to retrieve a username was successful and if doesn't, we prompt for a new username.
    else:
        # username = input("What is your name?")
        # filename = 'username.json'
        # with open(filename, 'w') as f:
        #     json.dump(username, f)
        #     print(f"We'll remember you when you come back, {username}!")
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        
greet_user()

