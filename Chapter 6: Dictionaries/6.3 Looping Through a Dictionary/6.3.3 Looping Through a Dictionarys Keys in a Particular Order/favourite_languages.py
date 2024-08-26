# Dictionaries - Looping Through a Dictionary - Looping Through a Dictionary's Keys in a Particular Order

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")