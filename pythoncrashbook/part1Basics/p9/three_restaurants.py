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


restaurant = Restaurant('McDonalds','Big mac')
print(f"The restaurant name is {restaurant.name}")
print(f"You ordered: {restaurant.dish}")
print("\n")
restaurant.open_restaurant()
print("\n")
restaurant.describe_restaurant()
print("\n1")
second_restaurant = Restaurant('BurgerKing','Whooper')
second_restaurant.describe_restaurant()
print("\n2")
second_restaurant = Restaurant('KFC','Chicken tenders')
second_restaurant.describe_restaurant()
print("\n3")
second_restaurant = Restaurant('Subway','SpicyItalian')
second_restaurant.describe_restaurant()
