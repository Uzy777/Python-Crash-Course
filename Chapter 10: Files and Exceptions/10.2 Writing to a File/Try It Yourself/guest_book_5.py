# 10-5. Guest Book:     Write a 'while loop' that prompts users for their name. Collect all the names that are entered,
#                       and then write these names to a file called 'guest_book.txt'. Make sure each entry appears on a new line in the file.

from pathlib import Path

path = Path('Chapter 10: Files and Exceptions/10.2 Writing to a File/Try It Yourself/guest_book.txt')

names = []

while True:
    name = input("What is your name? (Type 'quit' to exit) \n")
    
    if name.lower() == 'quit':
        break
    
    names.append(name)

path.write_text('\n'.join(names))