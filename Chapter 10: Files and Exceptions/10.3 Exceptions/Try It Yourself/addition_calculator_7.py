# 10-7. Addition Calculator:        Wrap your code from Exercise 10-6 in a 'while loop' so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please ensure you input a number!")
    else:
        print(answer)