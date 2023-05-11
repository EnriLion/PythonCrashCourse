class Privileges:
    """A class to show the privileges"""
    def show_privileges(self):
        """Shows the administrator's list of privileges"""

        self.privileges = ["can add post", "can delete post", "can ban user", "can forward a message", "can block user", "can delete user" ]

        print(f"These are your privileges:")
        for privilege in self.privileges:
            print("\n",privilege.title())

