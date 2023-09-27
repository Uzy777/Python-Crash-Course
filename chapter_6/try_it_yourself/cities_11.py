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