# 10-1. Learning Python:        Open a blank file in your text editor and write a few lines summarising what you've learned about Python so far.
#                               Start each line with the phrase "in Python you can..." Save the file as 'learning_python.txt'
#                               in the same directory as your exercises from this chapter. Write a program that reads the file and prints
#                               what you wrote two times: print the contents once by reading in the entire file, and once by storing the
#                               lines in a list and then looping over each line.

from pathlib import Path

print("Using the file to read the data:")
path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

"""Working with list section"""
print("\nUsing a for loop to read from a list:")
lines = contents
skills = ''
for line in lines:
    skills += line

print(skills)