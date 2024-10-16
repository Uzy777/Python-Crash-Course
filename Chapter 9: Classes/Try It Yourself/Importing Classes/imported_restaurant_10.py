# 9-10. Imported Restaurant:        Using your latest 'Restaurant' class, store it in a module. Make a separate file that imports 'Restaurant'.
#                                   Make a 'Restaurant' instance, and call one of 'Restaurants' methods to show that the 'import' statement is working properly.

from restaurant import Restaurant

restaurant = Restaurant('Cardiff BBQ House', 'BBQ Food')
restaurant.describe_restaurant()
restaurant.open_restaurant()