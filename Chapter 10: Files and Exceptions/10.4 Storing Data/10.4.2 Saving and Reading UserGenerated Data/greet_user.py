# Files and Exceptions - Storing Data - Saving and Reading User-Generated Data

from pathlib import Path
import json

path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/10.4.2 Saving and Reading UserGenerated Data/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")