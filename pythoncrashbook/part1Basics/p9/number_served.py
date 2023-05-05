class Restaurant:
    """A simple attempt to create a restaurant"""

    def __init__(self, name, dish):
        """Initialize the restaurant name and the dish name"""
        self.name = name
        self.dish = dish
        self.number_served = 0

    def describe_restaurant(self):
        """Print these two pieces of information"""
        print(f"This is the restaurant's {self.name}")
        print(f"This is your {self.dish}")

    def open_restaurant(self):
        """Simulate that the restaurant is open"""
        print(f"The restaurant is open")

    def read_number_served(self):
        """Print a statement showing the number served"""
        print(f"Number served: {self.number_served}")

    def set_number_served(self,number):
        """Let set the number of customers that have been served"""
        self.number_served = number

    def increment_number_served(self,number):
        """Increment the method with a new number served"""
        self.number_served += number



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
print("\n")
restaurant = Restaurant('PizzaHot','pepperoni pizza')
restaurant.read_number_served()
restaurant.number_served = 15

restaurant.read_number_served()
restaurant.number_served = 0

restaurant.set_number_served(100)
restaurant.read_number_served()

restaurant.set_number_served(20)
restaurant.read_number_served()

restaurant.increment_number_served(300)
restaurant.read_number_served()

print("\n")
