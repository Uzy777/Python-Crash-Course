# 10-13. User Dictionary:       The 'remember_me.py' example only stores on piece of information, the username.
#                               Expand this example by asking for two more pieces of information about the user,
#                               then store all the information you collect in a dictionary. Write this dictionary to a file using 'json.dumps()',
#                               and read it back in using 'json.loads'. Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json


path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/Try It Yourself/qualities.json')

if path.exists():
    contents = path.read_text()
    qualities = json.loads(contents)
    print(f"Welcombe back, {qualities['username']}!")
else:
    qualities = {}
    qualities["username"] = input("What is your name? ")
    qualities["colour"] = input("What is your favourite colour? ")
    qualities["number"] = input("What is your favourite number? ")
    contents = json.dumps(qualities)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {qualities['username']}!")

# Print the user's information
print(f"Your username is {qualities['username']}, your favourite colour is {qualities['colour']}, and your favourite number is {qualities['number']}!")
