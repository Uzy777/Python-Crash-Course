# 9-2. Three Restaurants:   Start with your class from Exercise 9-1. Create three different instances from the class,
#                           and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} and we have {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open!")

restaurant_1 = Restaurant('Cardiff BBQ House', 'BBQ')
restaurant_2 = Restaurant('Laketown', 'Fish')
restaurant_3 = Restaurant('Frenchtail Wave House', 'Vegan')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

