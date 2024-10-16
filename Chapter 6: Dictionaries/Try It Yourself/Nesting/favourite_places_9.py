# 6-9. Favourite Places:        Make a dictionary called 'favourite_places'. Think of three names to use as keys in the dictionary, and store one to three favourite places for each person.
#                               To make this exercise a bit more interesting, ask some friends to name a few of their favourite places. Loop through the dictionary,
#                               and print each person's name and their favourite places.

favourite_places = {
    'tim': ['UK', 'France', 'USA'],
    'becky': ['Spain', 'Japan'],
    'bill': ['UK'],
}

for fav, places in favourite_places.items():
    print(f"{fav.title()} loves the following places: {places}")