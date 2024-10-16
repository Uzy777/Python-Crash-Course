# 3-10. Every Function:     Think of things you could store in a list. For example, you could make a list of
#                           mountains, rivers, countries, cities, languages, or anything else you'd like.
#                           Write a program that creates a list containing these items and then uses
#                           each function introduced in this chapter at least once.

colours = ["Red", "Black", "Orange", "Green", "Yellow", "Blue", "White", "Brown"]

print(colours[1])

message = f"The best colour in the world is {colours[3]} says Bob!"
print(message)

colours[7] = "Pink"
print(colours)

colours.append("Purple")
print(colours)

colours.insert(0, "Gold")
print(colours)

del colours[3]
print(colours)

popped_colours = colours.pop()
print(colours)
print(popped_colours)

colours.remove("Gold")
print(colours)

colours.sort()
print(colours)


print(colours)
print(sorted(colours))

colours.reverse()
print(colours)

print(len(colours))