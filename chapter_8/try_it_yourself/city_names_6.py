# 8-6. City Names:  Write a function called city_country() that takes in the name of a city
#                   and its country. The function should rreturn a string formatted like this:
#                   "santiago, Chile"
#                   Call your function with at least three city-country pairs, and print the
#                   values that are returned.


def city_country(city_name, country_name):
    complete = f"{city_name} {country_name}"
    return complete.title()


final = city_country('tokyo', 'japan')
print(final)

final = city_country('paris', 'france')
print(final)

final = city_country('sydney', 'australia')
print(final)