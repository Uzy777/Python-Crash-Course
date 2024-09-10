from city_functions_2_2 import get_city_country


def test_city_country():
    """Does the names London, England work?"""
    formatted_name = get_city_country('london', 'england')
    assert formatted_name == 'London, England - Population = 5000000'