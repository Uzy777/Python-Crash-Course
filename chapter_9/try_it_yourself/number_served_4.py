# 9-4. Number Served:   Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served
#                       with a default value of 0. Create an instance called restaurant from this class. Print the 
#                       number of customers the restaurant has served, and then change this value and print it again.
#
#                       Add a method called set_number_served() That lets you set the number of customers that have been
#                       served. Call this method with a new number and print the value again.
#
#                       Add a method called increment_number_served() that lets you increment the number of customers who've been
#                       served. Call this method with any number you like that could represent how many customers were served in,
#                       say, a day of business.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} and we have {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open!")

    def restaurant(self):
        print(f"\nNumber of customers served {self.number_served}")

    def set_number_served(self):
        self.number_served = 33
        print(f"New number of customers served - {self.number_served}")

    def increment_number_served(self, served):
            self.number_served += served


restaurant = Restaurant('Cardiff BBQ House', 'BBQ')

print(f"This is my favouirte restaurant name - {restaurant.restaurant_name}!")
print(f"This is my favouirte type of cuisine - {restaurant.cuisine_type}!")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.restaurant()

restaurant.set_number_served()

restaurant.increment_number_served(89)
restaurant.restaurant()


