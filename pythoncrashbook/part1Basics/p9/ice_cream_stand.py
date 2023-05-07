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

    def describe_ice(self):
        """Simulate that describes the ice cream"""
        full_ice = f"Restaurant:{self.name}\nIce cream: {self.dish}"
        return full_ice

class IceCreamStand(Restaurant):
    """A simple attempt to create an ice cream stand"""

    def __init__(self, name, dish):
        """A simple attempt to create an ice cream stand"""
        super().__init__(name, dish)



restaurant = Restaurant('McDonalds','Big mac')
print(f"The restaurant name is {restaurant.name}")
print(f"You ordered: {restaurant.dish}")
print("\n")
restaurant.open_restaurant()
print("\n")
restaurant.describe_restaurant()
print("\n")
flavors = IceCreamStand('Kwality', 'LimaIcream')
print(flavors.describe_ice())

