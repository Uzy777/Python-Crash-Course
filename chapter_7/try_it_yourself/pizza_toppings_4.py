# 7-4. Pizza Toppings:  Write a loop that prompt the user to enter a series of pizza toppings
#                       until they enter a 'quit' value. As they enter each topping, print
#                       a message saying you'll add that topping to their pizza. 

prompt = "\nPlease enter the toppings you wish to have on your Pizza: "
prompt += "\nType 'quit' when your done entering toppings."

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"You want {topping.title()} on your Pizza.")
