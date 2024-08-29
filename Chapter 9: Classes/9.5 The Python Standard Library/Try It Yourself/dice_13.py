# 9-13. Dice:       Make a class 'Die' with one attribute called 'sides', which has a default value of 6.
#                   Write a method called 'roll_die()' that prints a random number between 1 and the number of sides the die has.
#                   Make a 6-sided die and roll it 10 times.
#                   Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


six_sided_die = Die()
ten_sided_die = Die(10)
twenty_sided_die = Die(20)


# Six sided die
print("SIX SIDED DIE (x10 rolls):")
for die in range(10):
    six_sided_die.roll_die()

# Ten sided die
print("TEN SIDED DIE (x10 rolls):")
for die in range(10):
    ten_sided_die.roll_die()

# Twenty sided die
print("TWENTY SIDED DIE (x10 rolls):")
for die in range(10):
    twenty_sided_die.roll_die()