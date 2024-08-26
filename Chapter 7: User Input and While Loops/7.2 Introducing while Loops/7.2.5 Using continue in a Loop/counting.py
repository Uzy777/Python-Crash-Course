# User Input and While Loops - Introducing while Loops - Using continue in a Loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)