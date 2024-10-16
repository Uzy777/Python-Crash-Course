# 5-11. Ordinal Numbers:        Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2 and 3.
#                               
#                               - Store the numbers 1 through 9 in a list.
#                               - Loop through the list.
#                               - Use an 'if-elif-else' chain inside the loop to print the proper ordinal ending for each number.
#                               Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

numbers = 1,2,3,4,5,6,7,8,9

for number in numbers:
    if 1 == number:
        print("1st")
    elif 2 == number:
        print("2nd")
    elif 3 == number:
        print("3rd")
    elif 4 == number:
        print("4th")
    elif 5 == number:
        print("5th")
    elif 6 == number:
        print("6th")
    elif 7 == number:
        print("7th")
    elif 8 == number:
        print("8th")
    elif 9 == number:
        print("9th")
