pizzas = ["Cheese", "Chicken", "Pepperoni"]

friend_pizzas = pizzas[:]

pizzas.append("Vegetable")
friend_pizzas.append("Bacon")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

