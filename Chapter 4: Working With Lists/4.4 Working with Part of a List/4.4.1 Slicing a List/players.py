# Slicing a List - Slicing is a method to extract a portion of a sequence (like a list or string) using the syntax sequence[start:stop].

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

###################################################################
# Slicing another index

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

###################################################################
# Slicing from beginning of the list index

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4])

###################################################################
# Slicing to the end of the list index

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:])

###################################################################
# Slicing the last three players

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-3:])