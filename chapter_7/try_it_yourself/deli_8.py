# 7-8. Deli:    Make a list called sandwich_orders and fill it with the names of various
#               sandwiches. Then make an empy list called finished_sandwiches.
#               Loop through the list of sandwich orders and print a message for each order,
#               such as I made your tuna sandwich. As each sandwich is made, move it to the
#               list of finished sandwiches. After all the sandwiches have been made,
#               print a message listing each sandwich that was made.


sandwich_orders = ['Cheese', 'Chicken', 'Tuna', 'Beef', 'Egg']
finished_sandwiches = []

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")

while sandwich_orders:
    finished = sandwich_orders.pop()

    finished_sandwiches.append(finished)

for made in finished_sandwiches:
    print(f"Your {made} sandwich has been made.")