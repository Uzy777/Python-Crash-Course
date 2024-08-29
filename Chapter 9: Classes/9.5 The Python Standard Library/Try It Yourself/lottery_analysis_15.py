# 9-15. Lottery Analysis:       You can use a loop to see how hard it might be to win the kind of lottery you ust modeled. Make a list or tuple called 'my_ticket'.
#                               Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to ru nto give you a winning ticket.

from random import choice

attempts = 0

letters_numbers = ['tim', 'ray', 'cat', 'chocolate', 'mango', 100, 77, 36, 1, 9, 3983, 1343, 832, 1298, 4]

my_ticket = ['ray', 'cat', 'mango', 77]


print("Any ticket matching these 4 numbers or letters wins a prize!")

while True:
    # This is a better way to write instead of each line with the for loop
    """Will loop through until a drawn ticket that matches my ticket is found.
    Then will stop and output the number of attempts taken"""
    drawn_ticket = [choice(letters_numbers) for _ in range(4)]
    attempts += 1
    if drawn_ticket == my_ticket:
        print("You are the winner! Congratulations")
        break
print(f"It took {attempts} to win the lottery with my ticket!")



# for winner in range(4):
#     winning_character = choice(letters_numbers)
#     print(winning_character)

