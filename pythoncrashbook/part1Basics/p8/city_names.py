def city_country(name, country):
    """A function to return the city name and country"""
    country_name = f"\n{name} {country}"
    return country_name.title()
count = city_country('santiago','chile')
print(count)
#country_pairs 2
count_2 = city_country('bogota','colombia')
print(count_2)
#country_pairs 3
count_3 = city_country('riyadh','arabia')
print(count_3)
