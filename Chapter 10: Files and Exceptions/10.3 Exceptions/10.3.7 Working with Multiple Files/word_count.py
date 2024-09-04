# Files and Exceptions - Exceptions - Working with Multiple Files

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    path = Path(f'Chapter 10: Files and Exceptions/10.3 Exceptions/10.3.7 Working with Multiple Files/{filename}')
    count_words(path)
