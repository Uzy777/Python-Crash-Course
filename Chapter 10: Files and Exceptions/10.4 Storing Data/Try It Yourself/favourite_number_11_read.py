# 10-11. Favourite Number:      Write a program that prompts for the user's favourite number. Use 'json.dumps()' to store this number in a file.
#                               Write a separate program that reads in this value and prints the message "I know your favourite number! It's ____".

from pathlib import Path
import json

path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/Try It Yourself/favourite_number.json')

contents = path.read_text()
numbers = json.loads(contents)

print(numbers)