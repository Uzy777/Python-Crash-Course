# 2-7. Stripping Names:     Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.
#                           Make sure you use each character combination, "\t" and "\n", at least once. Then print the name using each of the three
#                           stripping functions, 'lstrip()', 'rstrip()', and 'strip()'.

name = "\tMike Tyson\n"
print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())