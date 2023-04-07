rivers = {'nile': 'egypt', 'amazon': 'brazil', 'bravo' : 'mexico-usa'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\n")

for river in rivers.keys():
    print(f"The {river.title()} is amazing")
    

print("\n")

for country in rivers.values():
    print(f"The {country.title()} is an amazing country")


