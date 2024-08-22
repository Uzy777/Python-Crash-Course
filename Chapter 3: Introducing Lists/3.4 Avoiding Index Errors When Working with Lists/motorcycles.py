# Avoiding Index Errors When Working with Lists 

# This will error out has no entry of 3 exists
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[3])

###################################################################
# Also adding the following will error due to no items in the list

motorcycles2 = []
print(motorcycles2[-1])