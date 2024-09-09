# Files and Exceptions - Storing Data - Using json.dumps() and json.loads()

# from pathlib import Path
# import json

# numbers = [2, 3, 5 , 7, 11, 13]

# path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/10.4.1 Using json.dumps and json.loads/numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)

#########################################################

#

from pathlib import Path
import json

numbers = [2, 3, 5 , 7, 11, 13]

path = Path('Chapter 10: Files and Exceptions/10.4 Storing Data/10.4.1 Using json.dumps and json.loads/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)