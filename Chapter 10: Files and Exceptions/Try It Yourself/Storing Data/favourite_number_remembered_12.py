# 10-12. Favourite Number Remembered:       Combine the two programs you wrote in Exercise 10-11 into one file. If the number is already stored,
#                                           report the favourite number to the user. If not prompt for the user's favourite number and store it in a file.
#                                           Run the program twice to see that it works.

from pathlib import Path
import json

path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/Try It Yourself/favourite_number.json')
if path.exists():
    contents = path.read_text()
    favourite_number = json.loads(contents)
    print(f"Your favourite number is - {favourite_number}!")
else:
    favourite_number = input("What is your favourite number? ")
    contents = json.dumps(favourite_number)
    path.write_text(contents)
    print(f"I shall store you favourite number - {favourite_number}!")