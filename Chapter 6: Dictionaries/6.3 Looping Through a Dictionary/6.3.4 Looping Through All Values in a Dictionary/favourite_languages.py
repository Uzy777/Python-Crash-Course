# Dictionaries - Looping Through a Dictionary - Looping Through All Values in a Dictionary

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

###################################################################

#
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())