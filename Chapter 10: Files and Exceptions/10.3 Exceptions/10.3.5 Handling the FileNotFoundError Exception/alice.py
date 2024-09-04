# Files and Exceptions - Exceptions - Handling the FileNotFoundError Exception

from pathlib import Path

path = Path('Chapter 10: Files and Exceptions/10.3 Exceptions/10.3.5 Handling the FileNotFoundError Exception/alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")