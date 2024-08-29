# 9-14. Lottery:        Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list
#                       and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

from random import choice

letters_numbers = ['tim', 'ray', 'cat', 'chocolate', 'mango', 100, 77, 36, 1, 9, 3983, 1343, 832, 1298, 4]

print("Any ticket matching these 4 numbers or letters wins a prize!")
for winner in range(4):
    winning_character = choice(letters_numbers)
    print(winning_character)
