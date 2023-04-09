person = {'first_name': 'enrique', 'last_name': 'leon','age' : 20, 'city': 'estado'}

print(f"Your  first name is {person['first_name'].title()}")
print("\n")
print(f"Your  last name is {person['last_name'].title()}")
print("\n")
print(f"Your  age  {person['age']} and you lived in {person['city'].title()}")

print("\n")
person_1 = {'first_name': 'henry', 'last_name': 'toreto','age' : 25, 'city': 'angeles'}
person_2 = {'first_name': 'diego', 'last_name': 'chavez','age' : 21, 'city': 'ciudad'}
person_3 = {'first_name': 'enri', 'last_name': 'zevcha','age' : 15, 'city': 'estado'}

people = [person_1, person_2, person_3]

for peoples in people:
   print(f"Everyone is a human {peoples}" )
