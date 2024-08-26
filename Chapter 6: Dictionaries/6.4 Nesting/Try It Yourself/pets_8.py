# 6-8. Pets:        Make several dictionaries, where each dictionary represents a different pet.
#                   In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called 'pets'.
#                   Next, 'loop' through your list and as you do, print everything you know about each pet.

pet_0 = {'animal': 'Dog', 'owner': 'Tim',}
pet_1 = {'animal': 'Cat', 'owner': 'Rachel',}
pet_2 = {'animal': 'Shark', 'owner': 'Ben',}
pet_3 = {'animal': 'Bird', 'owner': 'Jess',}
pet_4 = {'animal': 'Lizard', 'owner': 'Cameron',}


pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nAnimal:", pet['animal'])
    print(f"Owner:", pet['owner'])