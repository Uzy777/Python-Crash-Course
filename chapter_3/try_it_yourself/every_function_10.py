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