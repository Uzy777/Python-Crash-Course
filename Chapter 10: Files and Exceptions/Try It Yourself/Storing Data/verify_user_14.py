# 10-14. Verify User:       The final listing for 'remember_me.py' assumes either that the user has already entered their username or
#                           that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/Try It Yourself/username.json')
    username = get_stored_username(path)
    if username:
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcombe back, {username}!")

        correct_username = input(f"Is this your username? - '{username}' (yes/no): ")
        if correct_username == "no":
            get_new_username(path)
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()