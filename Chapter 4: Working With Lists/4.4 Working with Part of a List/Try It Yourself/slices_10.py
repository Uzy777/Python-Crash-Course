# 4-10. Slices:     Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#
#                   - Print the message "The first three items in the list are:". Then use a slice to print the first three items from that program's list.
#                   - Print the message "Three items from the middle of the list are:". Then use a slice to print three items from the middle of the list.
#                   - Print the message "The last three items in the list are:". Then use a slice to print the last three items in the list.

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