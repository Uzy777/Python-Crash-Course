# Files and Exceptions - Writing to a File - Writing Multiple Lines

from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('Chapter 10: Files and Exceptions/10.2 Writing to a File/10.2.2 Writing Multiple Lines/programming.txt')

path.write_text(contents)
