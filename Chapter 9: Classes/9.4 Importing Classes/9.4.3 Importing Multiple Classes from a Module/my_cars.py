# Classes - Importing Classes - Importing Multiple Classes from a Module

from car import Car, ElectricCar

my_dream_car = Car('VW', 'Golf-R', 2017)
print(my_dream_car.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())