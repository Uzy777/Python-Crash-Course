# 6-3. Glossary:        A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
#                       
#                       - Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#                       - Print each word and its meaning as neatly formatted output You might print the word followed by a colon and then its meaning,
#                       or print the word on one line and then print its meaning indented on a second line.
#                       Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {'integer': 'Is a number', 'print': 'Outputs data for you',
            'list': 'Able to store multiple variables', 'string': 'Contains a number of letters',
            'loop': 'Continuously goes through a set of data'}

print(f"Integer: {glossary['integer']}")
print(f"\nPrint: {glossary['print']}")
print(f"\nList: {glossary['list']}")
print(f"\nString: {glossary['string']}")
print(f"\nLoop: {glossary['loop']}")


        