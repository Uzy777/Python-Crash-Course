# Classes - Creating and Using a Class - Making an Instance from a Class - Calling Methods

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
my_dog = Dog('Willie', 6)

my_dog.sit()
my_dog.roll_over()