# 8-5. Cities:  Write a function called describe_city() that accepts the name of
#               a city and its country. The function should pritn a simple sentence,
#               such as Reykjavik is in Iceland. Give the parameter for the country
#               a defautl value.
#               Call your function for three different cities, at least one of which
#               is not in the default country.


def describe_city(name_city, name_country='Cardiff'):
    print(f"{name_city.title()} is in {name_country.title()}!")

describe_city(name_city='Whitchurch')
describe_city(name_city='Grangetown')
describe_city(name_city='Istanbul', name_country='Turkey')