# Files and Exceptions - Storing Data - Saving and Reading User-Generated Data

# from pathlib import Path
# import json

# username = input("What is your name? ")

# path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/10.4.2 Saving and Reading UserGenerated Data/username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")


#########################################################
#

from pathlib import Path
import json

path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/10.4.2 Saving and Reading UserGenerated Data/username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcombe back, {username}!")
else:
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")