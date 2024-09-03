# 10-3. Simpler Code:       The program 'file_reader.py' in this section uses a temporary variable, lines, to show how 'splitlines()' works.
#                           You can skip the temporary variable and loop directly over the list that 'splitlines()' returns:
#                           
#                           for lien in contents.splitlines():
#                           
#                           Remove the temporary variable from each of the programs in this section, to make them more concise.

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)