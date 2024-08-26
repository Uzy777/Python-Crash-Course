# Dictionaries - Looping Through a Dictionary - Looping Through All Key-Value Pairs

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name,language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")