def get_formatted_country(city, country, population=''):
    """Generate a neatly formatted country and city"""
    if population:
        full_place = f"{city} {country} - {population}"
    else:
        full_place = f"{city} {country}"
    return full_place.title()

