# 7-10. Dream Vacation:     Write a program that polls users about their dream vacation. Write a prompt similar to if you could visit one place in the
#                           world, where would you go? Include a block of code that prints the results of the poll.

responses = {}

polling_active = True

while polling_active:
    name = input("\nInput your name: ")
    response = input("\nWhat is one country which you want to visit right now?: ")

    responses[name] = response

    repeat = input("Would you like anyone else to respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\nTHE POLLING RESULTS")
for name, response in responses.items():
    print(f"{name.title()}'s dream destination is to go to {response.title()}!")