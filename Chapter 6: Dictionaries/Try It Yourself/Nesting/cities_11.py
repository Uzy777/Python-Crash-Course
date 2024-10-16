# 6-11. Cities:         Make a dictionary called 'cities'. Use the names of three cities as keys in your dictionary.
#                       Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
#                       The keys for each city's dictionary should be something like 'country', 'population', and 'fact'.
#                       Print the name of each city and all of the information you have stored about it.

cities = {
    'New York City':{
        'country': 'USA',
        'population': '8.8m',
        'fact': 'NYC is incredibly diverse, with over 800 spoken languages.',
    },

    'Tokyo':{
        'country': 'Japan',
        'population': '13.5m',
        'fact': 'Tokyos Shibuya Crossing is the worlds busiest pedestrian intersection.',
    },

    'Paris':{
        'country': 'France',
        'population': '2.15m',
        'fact': 'Paris houses the Catacombs, an underground ossuary with millions of human remains.',
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()} has the following info:")
    print(f"\t{city_info['country']}")
    print(f"\t{city_info['population']}")
    print(f"\t{city_info['fact']}")