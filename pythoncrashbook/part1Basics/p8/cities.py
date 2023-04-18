def describe_city(name, city):
    """ A function to describe a city"""
    print(f"\n{name.title()} is in {city.title()}")
describe_city('elias','mexico')

def describe_city(name, city='mexico'):
    """ A function to describe a city"""
    print(f"\n{name.title()} is in {city.title()}")
describe_city('elias')

