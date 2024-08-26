# Dictionaries - Looping Through a Dictionary - Looping Through All the Keys in a Dictionary

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favourite_languages.keys():
    print(name.title())

###################################################################

#
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

###################################################################

#
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")