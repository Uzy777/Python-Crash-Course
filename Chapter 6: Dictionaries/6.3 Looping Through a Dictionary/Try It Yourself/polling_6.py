# 6-6. Polling:     Use the code in 'favourite_languages.py'.
#
#                   - Make a list of people who should take the favourite languages poll. Include some names that are already in the dictionary and some that are not.
#                   - Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.
#                   If they have not yet taken the poll, print a message inviting them to take the poll.

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