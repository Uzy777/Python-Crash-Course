# Dictionaries - Nesting - A List of Dictionaries

# alien_0 = {'colour': 'green', 'points': 5}
# alien_1 = {'colour': 'yellow', 'points': 10}
# alien_2 = {'colour': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

###################################################################

# # Make an empty list for storing aliens
# aliens = []

# # Make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'colour': 'green', 'points': '5', 'speed': 'slow'}
#     aliens.append(new_alien)

# # Show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # Show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}")

###################################################################

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 3 aliens with the characteristics
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

