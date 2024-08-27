# 9-6. Ice Cream Stand:         An ice cream stand is a specific kind of restaurant. Write a class called 'IceCreamStand' that inherits
#                               from the 'Restaurant' class you wrote in Exercise 9-1 or Exercise 9-4. Either version of the class will work;
#                               just pick the one you like better. Add an attribute called 'flavours' that stores a list of ice cream flavours.
#                               Write a method that displays these flavours. Create an instance of 'IceCreamStand', and call this method.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name} and we have {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'vanilla', 'strawberry']
    
    def display_flavours(self):
        """Display the list of ice cream flavours."""
        print(f"These are the flavours we have {self.flavours}")


# Create an instance of IceCreamStand
my_ice_cream_stand = IceCreamStand('Cool Cones', 'Ice Cream')

# Call the method to display flavours
my_ice_cream_stand.display_flavours()