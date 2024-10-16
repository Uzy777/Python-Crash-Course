# 9-1. Restaurant:  Make a class called Restaurant. The __init__() method for Restaurant should store two
#                   attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
#                   that prints these two pieces of information, and a method called open_restaurant() that prints a message
#                   indicating that the restaurant is open.
#                   Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} and we have {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open!")

restaurant = Restaurant('Cardiff BBQ House', 'BBQ')

print(f"This is my favouirte restaurant name - {restaurant.restaurant_name}!")
print(f"This is my favouirte type of cuisine - {restaurant.cuisine_type}!")

restaurant.describe_restaurant()
restaurant.open_restaurant()