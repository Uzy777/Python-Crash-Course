# 7-1. Rental Car:  Wire a program that asks the user what kind of rental car they would like.
#                   Print a message about that car, such as "Let me see if I can find you a Subaru."

rental = input("What care are you looking to rent? ")
rental = print(f"\nLet me see if I can find you a {rental.title()}.")
