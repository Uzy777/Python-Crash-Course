# 10-10. Common Words:      Visit Project Gutenberg (https://gutenberg.org) and find a few texts you'd like to analyse.
#                           Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
#                           You can sue the count() method to find out how many times a word or phrase appears in a string.
#                           For example, the following code counts the number of times 'row' appears in a string:
# 
#                           line = "Row, row, row your boat"
#                           line.count('row')
#                       2
#                           line.lower().count('row')
#                       3
#       
#                           Notice that converting the string to lowercase using 'lower()' catches all appearances of the word you're looking for,
#                           regardless of how it's formatted. Write a program that reads the files you found at Project Gutenberg and determines
#                           how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'.
#                           Try counting 'the ', with a space in the string, and see how much lower your count is.

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        print("Number of words that contain 'the' in the book:")
        num_words = words.count('the')
        print(f"The file {path} has about {num_words} words.\n")

filenames = ['middlemarch.txt', 'pride_and_prejudice.txt', 'romeo_and_juliet.txt']

for filename in filenames:
    path = Path(f'Chapter 10: Files and Exceptions/10.3 Exceptions/Try It Yourself/{filename}')
    count_words(path)