class User:
    """A class attempt to make a logging"""
    def __init__(self, first_name, last_name, password, email):
        """Initialize first, last name, password and email"""

        self.first_name = first_name
        self.last_name = last_name
        self.password = password 
        self.email = email 
        self.login_attempts = 0


    def describe_user(self):
        """Prints a summary of the user's information"""

        print(f"First name:  {self.first_name}")
        print(f"Last name:  {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")


    def greet_user(self):
        """Prints a greeting to the user"""
        print(f"\nWelcome {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self,number):
        """Increment the value of login_attempts by 1"""
        self.login_attempts += number
        print(number)

    def reset_login_attempts(self):
        """Increment the value of login_attempts by 1"""
        self.login_attempts = 0
        print(self.login_attempts)


one_user = User('enrique', 'leon', 'akldjklasjdk', 'enriqueleon0201leon@gmail.com')
second_user = User('richy', 'morty', 'kjljdskla', 'mortyrichy12@protonmail.com')
third_user = User('viole', 'martinez', 'dajkdljasdas', 'kittymartinez32@gmail.com')

print("\n")
one_user.describe_user()
one_user.greet_user()
print("\n")
second_user.describe_user()
second_user.greet_user()
print("\n")
third_user.describe_user()
third_user.greet_user()
print("\n")
other_user = User('enri', 'hello', 'dajkdljasdas', 'enri3@protonmail.com')
print("\n")
other_user.increment_login_attempts(13)
other_user.reset_login_attempts()
other_user.reset_login_attempts()
