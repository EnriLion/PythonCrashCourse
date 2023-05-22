#Saving and reading user-generated data
#Where we primpt the user for their name the first time they run a program and then remember their name when they run the program again.
import json

username = input("What is your name? ")#we prompt for a username to store


filename = 'username.json'

# with open(filename, 'w') as f:
#     json.dump(username, f)# passing it a username and a file object to store the username
#     print(f"We'll remember you when you come back, {username}!")#We print the message informing

#We are going to modify our program to recognize the string(user)
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

