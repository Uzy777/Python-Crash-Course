# 5-5. Alien Colors #3:         Turn your 'if-else' chain from Exercise 5-4 into an if-elif-else chain.
#
#                               - If the alien is green, print a message that the player earned 5 points.
#                               - If the alien is yellow, print a message that the player earned 10 points.
#                               - If the alien is red, print a message that the player earned 15 points.
#                               - Write three versions of this program, making sure each message is printed for the appropriate colour alien.


alien_colour = "green"
if "green" in alien_colour:
    print("You just earned 5 points!")
elif "yellow" in alien_colour:
    print("You just earned 10 points!")
elif "red" in alien_colour:
    print("You just earned 15 points!")
else:
    print("You didn't earn any points!")

#----------------------------#

alien_colour = "yellow"
if "green" in alien_colour:
    print("You just earned 5 points!")
elif "yellow" in alien_colour:
    print("You just earned 10 points!")
elif "red" in alien_colour:
    print("You just earned 15 points!")
else:
    print("You didn't earn any points!")

#----------------------------#

alien_colour = "red"
if "green" in alien_colour:
    print("You just earned 5 points!")
elif "yellow" in alien_colour:
    print("You just earned 10 points!")
elif "red" in alien_colour:
    print("You just earned 15 points!")
else:
    print("You didn't earn any points!")