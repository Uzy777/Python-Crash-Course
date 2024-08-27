# Classes - Inheritance - Overriding Methods from the Parent Class

# If the parent class Car has a method called fill_gas_tank() this would not be required for the child class ElectricCar so you can override it.
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} mile on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_fuel_tank(self):
        """Electric cars don't have fuel tanks"""
        print("This car doesn't have a fuel tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_fuel_tank()