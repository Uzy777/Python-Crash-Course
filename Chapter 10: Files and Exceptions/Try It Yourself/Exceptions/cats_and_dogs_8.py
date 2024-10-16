# 10-8. Cats and Dogs:      Make two files, 'cats.txt' and 'dogs.txt'. Store at least three names of cats in the first file and three names of dogs in the second file.
#                           Write a program that tries to read these files and print the contents of the file to the screen.
#                           Wrap your code in a 'try-except' block to catch the 'FileNotFound' error, and print a friendly message if a file is missing.
#                           Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

from pathlib import Path

cat = Path('Chapter 10: Files and Exceptions/10.3 Exceptions/Try It Yourself/cats.txt')
dog = Path('Chapter 10: Files and Exceptions/10.3 Exceptions/Try It Yourself/dogs.txt')

print("List of Cat names:")
try:
    contents1 = cat.read_text()
    print(contents1)
except FileNotFoundError:
    print(f"Unable to read the file: {cat}")

print("\nList of Dog names:")
try:
    contents2 = dog.read_text()
    print(contents2)
except FileNotFoundError:
    print(f"Unable to read the file: {dog}")