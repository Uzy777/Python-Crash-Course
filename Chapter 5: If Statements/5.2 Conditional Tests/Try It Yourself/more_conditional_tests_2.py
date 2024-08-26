# 5-2. More Conditional Tests:      You don't have to limit the number of tets you create to 10. If you want to try more comparisons,
#                                   write more tests and add them to "more_conditional_tests.py". Have at least one 'True' and one 'False' result for each of the following:
#                                   
#                                   - Tests for equality and inequality with strings
#                                   - Tests using the 'lower()' method
#                                   - Numerical tets involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
#                                   - Tests using the and keyword and the or keyword
#                                   - Test whether an item is in a list
#                                   - Test wether an item is not in a list


# Tests for equality and inequality with strings
animal_1 = "bear"
if animal_1 == "bear":
    print(f"We spotted the {animal_1}!")
else:
    print(f"We didn't spot a {animal_1}!")


animal_2 = "chicken"
if animal_2 != "lion":
    print(f"This is not the correct animal {animal_2}!")
else:
    print(f"We spotted the {animal_2}!")


#---------------------#

# Tests using the lower() method
car = "BMW"
print("\nThis car does not match:")
print(car.lower() == "BMW")

print("\nThis car does match:")
print(car.lower() == "bmw")


#---------------------#

# Numerical tests involving equality and inequality, greater than and less than, greater than or
# equal to, and less than or equal to
age = 19
print("\nAre you 19 years old?:")
print(age == 19)

print("\nAre you SURE your 19 years old?:")
print(age != 19)


print("\nAre you over 17 years old?:")
print(age > 17)

print("\nAre you less than 7 years old?:")
age = 5
print(age < 7)


print("\nAre you over 21 years old or over?:")
age = 21
print(age >= 21)

print("\nAre you over 21 years old or over?:")
age = 20
print(age >= 21)


print("\nAre you over 18 years old or under?:")
age = 18
print(age <= 18)

print("\nAre you over 18 years old or under?:")
age = 99
print(age <= 18)


#---------------------#

#Tests using the AND keyword and the OR keyword
colour_1 = "blue"
colour_2 = "pink"
colour_3 = "yellow"
print("\nAre the colours blue and pink available to use?:")
print(colour_1 == "blue" and colour_2 == "pink")

print("\nAre the colours yellow or orange available to use?:")
print(colour_3 == "yellow" or colour_4 == "orange")


#---------------------#

# Test whether an item is in a list
colours = ["red", "green", "blue", "orange", "yellow", "purple"]
print("\nDo we have a red pencil somewhere?:")
print("red" in colours)


#---------------------#

# Test whether an item is not in a list
colours = ["red", "green", "blue", "orange", "yellow", "purple"]
print("\nIs the white pencil missing?:")
print("white" not in colours)