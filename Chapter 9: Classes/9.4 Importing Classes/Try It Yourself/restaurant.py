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