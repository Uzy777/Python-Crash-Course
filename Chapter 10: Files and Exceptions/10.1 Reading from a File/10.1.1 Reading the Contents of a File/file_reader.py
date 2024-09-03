# Files and Exceptions - Reading from a File - Reading the Contents of a File

# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()

# print(contents)


###################################################################

# Stripping whitespace
# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip()

# print(contents)


###################################################################

# Stripping trailing newline
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

print(contents)