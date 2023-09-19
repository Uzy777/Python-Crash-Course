favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

favourite_languages_to_take = ['bill', 'harry', 'phil', 'jen']

for name in favourite_languages_to_take:
    print(f"Please {name.title()} take the poll!")
    if name in favourite_languages.keys():
        print(f"\tThank you {name.title()} for responding.")