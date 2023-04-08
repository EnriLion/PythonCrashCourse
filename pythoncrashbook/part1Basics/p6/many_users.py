#A dictionary in a dictionary
#You can nest a dictionary inside another dictionary.
#But your code can get complicated quickly when you do

users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },
        }
for username, user_info in users.items():# we loop through the users
    print(f"\nUsername: {username}")#we print the user name
    full_name = f"{user_info['first']} {user_info['last']}"#we start accessing the inner dictionary. The variable user_info which contains the dictionary of user information, has three keys: 'first', 'last' and 'location'
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")# We use each key to generate a neatly formated full name and location for each person and we print a summary of what we know
    print(f"\tLocation: {location.title()}")

#The value associated with each key is a dictionary that includes each user's first anme and location

