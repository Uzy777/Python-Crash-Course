# 7-6. Three Exits:     Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
#
#                       - Use a conditional test in the while statement to stop the loop.
#                       - Use an active variable to control how long the loop runs.
#                       - Use a break statement to exit the loop when the user enters a 'quit' value.

# Use a conditional test in the while statement to stop the loop.
prompt = "\nPlease enter the toppings you wish to have on your Pizza: (You can only pick x4)"
prompt += "\nType 'quit' when your done entering toppings. "

count = 0

while count < 4:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You want {topping.title()} on your Pizza.")
        count += 1



# Use an active variable to control how long the loop runs.
prompt = "\nPlease enter the topping you wish to have on your Pizza: "
prompt += "\nType 'quit' when your done entering toppings. "

active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You want {topping.title()} on your Pizza.")
        active = False



# Use a break statement to exit the loop when the user enters a 'quit' value.
prompt = "\nPlease enter the toppings you wish to have on your Pizza: "
prompt += "\nType 'quit' when your done entering toppings."

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You want {topping.title()} on your Pizza.")