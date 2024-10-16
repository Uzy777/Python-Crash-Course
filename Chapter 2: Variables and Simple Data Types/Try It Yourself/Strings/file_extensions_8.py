# 2-8. File Extensions:     Python has a 'removesuffix()' method that works exactly like 'removeprefix()'. Assign the value 'python_notes.txt' to a 
#                           variable called filename. Then use the 'removesuffix()' method to display the filename without the file extension, like some file browsers do.

filename = "python_notes.txt"
remove  = filename.removesuffix('.txt')
print(remove)