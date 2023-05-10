class Restaurant:
    """A simple attempt to create a restaurant"""

    def __init__(self, name, dish):
        """Initialize the restaurant name and the dish name"""
        self.name = name
        self.dish = dish

    def describe_restaurant(self):
        """Print these two pieces of information"""
        print(f"This is the restaurant's {self.name}")
        print(f"This is your {self.dish}")

    def open_restaurant(self):
        """Simulate that the restaurant is open"""
        print(f"The restaurant is open")

