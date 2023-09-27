# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# language = favourite_languages['sarah'].title()
# print(f"Sarah's favourite language is {language}.")


#----------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name,language in favourite_languages.items():
#     print(f"{name.title()}'s favourite language is {language.title()}.")


#------------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in favourite_languages.keys():
#     print(name.title())


#-----------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']
# for name in favourite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favourite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")


#-----------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# if 'erin' not in favourite_languages.keys():
#     print("Erin, please take our poll!")


#---------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in sorted(favourite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


#-----------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favourite_languages.values():
#     print(language.title())


#---------------------------------------------#

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in set(favourite_languages.values()):
#     print(language.title())


#---------------------------------------------#

favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")