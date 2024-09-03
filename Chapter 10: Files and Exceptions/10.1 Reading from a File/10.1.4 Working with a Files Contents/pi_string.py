# Files and Exceptions - Reading from a File - Working with a Files Contents

# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line

# print(pi_string)
# print(len(pi_string))


###################################################################

# Using lstrip to get rid of whitespace
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))