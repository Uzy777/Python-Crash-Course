# 8-15. Printing Models:    Put the functions for the example printing_models.py in a separate file
#                           called printing_functions.py. Write an import statement at the top of
#                           printing_modules.py, and modify the file to use the imported functions.

from printing_functions import print_models, show_completed_models

# List of unprinted designs and an empty list for completed models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the functions to print models and show completed ones
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
