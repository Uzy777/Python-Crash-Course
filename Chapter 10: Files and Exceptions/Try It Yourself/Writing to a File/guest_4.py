# 10-4. Guest:      Write a program that prompts the user for their name. When they respond, write their name to a file called 'guest.txt'

from pathlib import Path

path = Path('Chapter 10: Files and Exceptions/10.2 Writing to a File/Try It Yourself/guest.txt')

name = input("What is your name: ")

path.write_text(name)