# Files and Exceptions - Storing Data - Refactoring

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
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
    path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/10.4.2 Saving and Reading UserGenerated Data/username.json')
    username = get_stored_username(path)
    if username:
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcombe back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()