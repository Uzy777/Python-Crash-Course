# 10-9. Silent Cats and Dogs:       Modify your except block in Exercise 10-8 to fail silently if either file is missing.

from pathlib import Path

cat = Path('Chapter 10: Files and Exceptions/10.3 Exceptions/Try It Yourself/cats.txt')
dog = Path('Chapter 10: Files and Exceptions/10.3 Exceptions/Try It Yourself/dogs.txt')

print("List of Cat names:")
try:
    contents1 = cat.read_text()
    print(contents1)
except FileNotFoundError:
    pass

print("\nList of Dog names:")
try:
    contents2 = dog.read_text()
    print(contents2)
except FileNotFoundError:
    pass