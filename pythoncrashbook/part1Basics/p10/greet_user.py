import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)#we use json.load() to read the information store in username.json and assing it to the varible username
    print(f"Welcome back, {username}!")#We've recovered the username.
