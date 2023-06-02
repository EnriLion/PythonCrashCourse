class Employee:
    """Describe a class representing an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Describe each attribute of the employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Adds annual salary to the user"""
        self.annual_salary += raise_amount


