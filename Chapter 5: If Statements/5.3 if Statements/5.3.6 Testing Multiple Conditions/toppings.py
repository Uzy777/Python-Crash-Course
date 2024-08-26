# If Statements - if statements - Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding Mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding Pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding Extra Cheese.")

print("\nFinished making your pizza!")

###################################################################

#
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding Mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding Pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding Extra Cheese.")

print("\nFinished making your pizza!")