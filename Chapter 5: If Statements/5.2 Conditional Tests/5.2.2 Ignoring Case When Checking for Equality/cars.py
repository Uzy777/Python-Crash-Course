# If Statements - Conditional Tests - Ignoring Case When Checking for Equality

# FALSE
car = 'Audi'
print (car == 'audi')

###################################################################

# TRUE
car = 'bmw'
print (car == 'bmw')

###################################################################

# TRUE - Using the lower() method does nto change the value that was originally stored in car
car = 'Audi'
print(car.lower() == 'audi')
print(car)