# Removing an Item Using the 'pop()' Method

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

###################################################################

# Assume motorcycles are in chronological order using 'pop()' we can print a statement about the last motorcycle bought.

motorcycles = ["honda", "yamaha", "suzuki"]

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")