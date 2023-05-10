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

class Admin(User):
    """A class attempt to make an admin user"""
    def __init__(self, first_name, last_name, password, email):
        """Initialize and inherits the father class"""
        super().__init__(first_name, last_name, password, email)
        self.priv = Privileges()

class Privileges:
    """A class to show the privileges"""
    def show_privileges(self):
        """Shows the administrator's list of privileges"""

        self.privileges = ["can add post", "can delete post", "can ban user", "can forward a message", "can block user", "can delete user" ]

        print(f"These are your privileges:")
        for privilege in self.privileges:
            print("\n",privilege.title())

    
    
one_user = User('enrique', 'leon', 'akldjklasjdk', 'enriqueleon0201leon@gmail.com')
second_user = User('richy', 'morty', 'kjljdskla', 'mortyrichy12@protonmail.com')
third_user = User('viole', 'martinez', 'dajkdljasdas', 'kittymartinez32@gmail.com')

admin = Admin('enrique', 'chavez', 'jrwerew', 'enri@192.168.1.com')

admin_privilege = Admin('enrique', 'chavez', 'jrwerew', 'enri@192.168.1.com')

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
# admin.show_privileges()
print("\n")
admin_privilege.priv.show_privileges()
