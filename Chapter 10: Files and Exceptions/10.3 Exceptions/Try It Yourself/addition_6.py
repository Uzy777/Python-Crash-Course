# 10-6. Addition:       One common problem when prompting for numerical input occurs when people provide text instead of numbers.
#                       When you try to convert the input to an 'int', you'll get a 'ValueError'. Write a program that prompts for two numbers.
#                       Add them together and print the result. Catch the 'ValueError' if either input is not a number, and print a friendly error message.
#                       Test you program by entering two numbers and then by entering some text instead of a number.

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

first_number = input("\nFirst number: ")
    
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please ensure you input a number!")
else:
    print(answer)