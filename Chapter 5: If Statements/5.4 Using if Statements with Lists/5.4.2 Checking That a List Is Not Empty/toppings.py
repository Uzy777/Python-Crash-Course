# If Statements - Using if Statements with Lists - Checking That a List Is Not Empty

requested_topping = []

if requested_topping:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
