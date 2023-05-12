def greet_user(username):
    """Display a simple greetimg.""" #this is called a docstring, whcih describe what the function does( are enclosed in triple quotes)
    print(f"Hello, {username.title()}!")


def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted."""
    full_name =f"{first_name} {last_name}"
    return full_name.title()

