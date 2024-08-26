# 6-4. Glossary 2:      Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of 'print()' calls
#                       with a loop that runs through the dictionary's keys  and values. When you're sure that your loop works, add five more Python terms to your glossary.
#                       When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {'integer': 'Is a number', 'print': 'Outputs data for you',
            'list': 'Able to store multiple variables', 'string': 'Contains a number of letters',
            'loop': 'Continuously goes through a set of data', 'python': 'Is a programming language',
            'sort': 'Is a function which can remove duplicate data',
            'dictionary': 'Consists of a key and a value',
            'pop': 'Delete, but can still be called in the program and used',
            'syntax': 'The actual coding structure that is used and formatted'}

for key, value in glossary.items():
    print(f"{key.title()}: {value}.")


        