from restaurant import Restaurant 

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
