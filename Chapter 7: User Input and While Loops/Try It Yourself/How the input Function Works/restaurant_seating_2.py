# 7-2. Restaurant Seating:  Wire a program that asks the user how many people are in their dinner group.
#                           If the answer is more than eight, print a message saying they'll have to
#                           wait for a table. Otherwise, report that their table is ready.

dinner_group = input("Hi, may I know how many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group >= 9:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")