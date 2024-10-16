# 7-9. No Pastrami:     Using the list sandwich_orders from Exercise 7-8, make sure the
#                       sandwich 'pastrami' appears in the list at least three times. Add
#                       code near the beginning of your program to print a message saying
#                       the deli has run out of pastrami, and then use a while loop
#                       to remove all occurrences of 'pastrami' from sandwich_orders.
#                       Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['Cheese', 'Chicken', 'Tuna', 'Beef', 'Egg', 'Pastrami', 'Pastrami', 'Pastrami']
finished_sandwiches = []

print("The Deli has run out of Pastrami sandwiches!")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")

while sandwich_orders:
    finished = sandwich_orders.pop()

    finished_sandwiches.append(finished)

for made in finished_sandwiches:
    print(f"Your {made} sandwich has been made.")