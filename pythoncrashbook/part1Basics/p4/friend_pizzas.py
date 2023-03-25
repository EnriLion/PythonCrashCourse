pizzas = [ 'pepperoni', 'hawaian', 'mexican' ]

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
    print(f"Nothing is better than your favorite pizza")
print("\nI really love pizza")

#4-11 My pizzas, your pizzas

pizzas.append('cheese')

friends_pizzas = pizzas[:]

friends_pizzas.insert(4, 'meat')

print(friends_pizzas)

#loops

for friends in friends_pizzas:
    print("\nMy friends favorite pizzas are:", friends)


for mypizzas in pizzas:
    print("\n",f"My favorite pizzas are {mypizzas.title()}")



