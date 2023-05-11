class User:
    """A class attempt to make a logging"""
    def __init__(self, first_name, last_name, password, email):
        """Initialize first, last name, password and email"""

        self.first_name = first_name
        self.last_name = last_name
        self.password = password 
        self.email = email 

    def describe_user(self):
        """Prints a summary of the user's information"""

        print(f"First name:  {self.first_name}")
        print(f"Last name:  {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")


    def greet_user(self):
        """Prints a greeting to the user"""
        print(f"\nWelcome {self.first_name.title()} {self.last_name.title()}!")
