# 6-7. People:      Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called 'people'.
#                   Loop through your list of people. As you loop through the list, print everything you know about each person.

person_0 = {'first_name': 'Tom', 'last_name': 'Rodger', 'age': 21, 'city': 'Cardiff'}
person_1 = {'first_name': 'Phil', 'last_name': 'Nope', 'age': 49, 'city': 'London'}
person_2 = {'first_name': 'Lex', 'last_name': 'Mex', 'age': 24, 'city': 'Manchester'}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\nFirst name:", person['first_name'])
    print(f"Last name:", person['last_name'])
    print(f"Age:", person['age'])
    print(f"City:", person['city'])