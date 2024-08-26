# Functions - Passing Arguments - Avoiding Argument Errors

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()



# line 8, in <module>
#     describe_pet()
# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'