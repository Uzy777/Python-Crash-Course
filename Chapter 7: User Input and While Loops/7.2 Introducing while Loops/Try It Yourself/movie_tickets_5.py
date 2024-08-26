# 7-5. Movie Tickets:   A movie theater charges different ticket prices depending on a person's age.
#                       If a person is under the age of 3, the ticket is free; if they are between
#                       3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
#                       Write a loop in which you ask users their age, and then tell them the cost
#                       of their movie ticket.

prompt = "\nNeed help finding out the price of your ticket?"
prompt += "\nHow old are you? "

while True:
    age = input(prompt)
    age = int(age)

    if age <= 3:
        print("Your ticket is going to be FREE!")

    elif age <= 12:
        print("Your ticket is going to be $10.")
    
    elif age > 12:
        print("Your ticket is going to be $15.")
