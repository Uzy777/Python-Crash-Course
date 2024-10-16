def get_city_country(city, country, population='5000000'):
    """Get a city and country from the user and store it"""
    city_country = f"{city}, {country} - population = {population}"
    return city_country.title()