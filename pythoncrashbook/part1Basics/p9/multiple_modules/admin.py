from user import User as U
from my_privileges import Privileges as P
class Admin(U):
    """A class attempt to make an admin user"""
    def __init__(self, first_name, last_name, password, email):
        """Initialize and inherits the father class"""
        super().__init__(first_name, last_name, password, email)
        self.priv = P()

