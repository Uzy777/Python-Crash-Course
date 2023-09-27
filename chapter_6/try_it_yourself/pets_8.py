pet_0 = {'animal': 'Dog', 'owner': 'Tim',}
pet_1 = {'animal': 'Cat', 'owner': 'Rachel',}
pet_2 = {'animal': 'Shark', 'owner': 'Ben',}
pet_3 = {'animal': 'Bird', 'owner': 'Jess',}
pet_4 = {'animal': 'Lizard', 'owner': 'Cameron',}


pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nAnimal:", pet['animal'])
    print(f"Owner:", pet['owner'])