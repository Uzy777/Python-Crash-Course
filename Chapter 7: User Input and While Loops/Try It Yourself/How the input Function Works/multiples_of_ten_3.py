# 7-3. Multiples of Ten:        Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("Can you give me a number please! ")
number = int(number)

if number % 10 == 0:
    print("You're number is a multiple of 10!")
else:
    print("You're number is not a multiple of 10!")