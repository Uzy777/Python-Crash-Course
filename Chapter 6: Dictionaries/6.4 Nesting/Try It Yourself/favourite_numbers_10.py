# 6-10. Favourite Numbers:      Modify your program from Exercise 6-2 so each person can have more than one favourite number. Then print each person's name along with their favourite numbers.

favourite_numbers = {'dave': [7, 99, 666], 'ellie': [21, 54, 83], 'jake': [99, 1],
                    'bex': 0, 'sam': [21, 22, 23]}

for fav, numbers in favourite_numbers.items():
    print(f"{fav.title()}'s favourite numbers are: {numbers}")