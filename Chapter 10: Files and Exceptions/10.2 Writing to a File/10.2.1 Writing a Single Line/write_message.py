# Files and Exceptions - Writing to a File - Writing a Single Line

from pathlib import Path

path = Path('Chapter 10: Files and Exceptions/10.2 Writing to a File/10.2.1 Writing a Single Line/programming.txt')
path.write_text("I love programming.")