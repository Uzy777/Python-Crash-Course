my_foods = ["pizza", "falafel", "carrot cake", "burger", "chips"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
my_foods.append("chicken")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#------------------#

print("\nThe first three items in my list are:")
print(my_foods[:3])

print("\nThree items from the middle of my list are:")
print(my_foods[2:5])

print("\nThe last three items in my list are:")
print(my_foods[4:7])