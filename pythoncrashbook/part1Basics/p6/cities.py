cities = {
        'mexico city': {
            'country': 'mexico',
            'population': '8.855 million',
            'fact': 'is skinking every year',
            },
        'mexico' : {
            'country' : 'mexico',
            'population': '126.7 million',
            'fact': 'is home to the worlds largest pyramid'
            },
        'new york': {
            'country': 'usa',
            'population': '8.468 million',
            'fact': 'is home to the worlds most famous city "centre Park"',
            },
        }

for city, country in cities.items():
    print(f"\nCity: {city}")
    print(f"\tCountry: {country['country']}")
    print(f"\tPopulation: {country['population']}")
    print(f"\tFact: {country['fact']}")
