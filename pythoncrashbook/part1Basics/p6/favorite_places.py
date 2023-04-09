favorite_places = {
        'arturo': ['cancun', 'paris'],
        'enrique': ['cdmx', 'new jork'],
        'miguel': ['cmdx', 'cancun', 'puerto vallarta'],
        'adrian': ['hidalgo', 'cdmx', 'cancun', 'veracruz'],
        }

for names, places in favorite_places.items():
    print(f"\n{names.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
