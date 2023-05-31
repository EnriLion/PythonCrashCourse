import json
def get_stored_username():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Write yes/YES or not/Not and hit ENTER")
        goodname = input(f"\nThis is your real name {username.title()} ")
        if goodname == 'yes' or goodname == 'YES':
            print(f"Welcome back, {username}!")
        elif goodname == 'not' or goodname == 'NOT':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username.title() }!")
        else:
            print(f"You didn't write yes/yes or not/NOT")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}! ")

greet_user()


