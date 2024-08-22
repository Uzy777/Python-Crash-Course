# 3-6. More Guests:     You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#                       
#                       - Start with your program from Exercise 3-4 or 3-5. Add a 'print()' call to the end of your program,
#                       informing people that you found a bigger table
#                       - Use 'insert()' to add one new guest to the beginning of your list.
#                       - Use 'insert()' to add one new guest to the middle of your list.
#                       - Use 'append()' to add one new guest to the end of your list.
#                       - Print a new set of invitation messages, one for each person in your list.


invite = ["Ali", "Mike", "Khabib"]
print(f"{invite[0]} you are invited to dinner!")
print(f"{invite[1]} you are invited to dinner!")
print(f"{invite[2]} you are invited to dinner!")

print(f"\nSadly our guest {invite[1]} can not make it for dinner.\n")

invite[1] = "Beth"
print(f"{invite[0]} you are invited to dinner!")
print(f"{invite[1]} you are invited to dinner!")
print(f"{invite[2]} you are invited to dinner!")

print("\nI have found a bigger table so more guests are invited to dinner!\n")

invite.insert(0, "Becky")
invite.insert(2, "James")
invite.insert(5, "Rodger")

print(f"{invite[0]} you are invited to dinner!")
print(f"{invite[1]} you are invited to dinner!")
print(f"{invite[2]} you are invited to dinner!")
print(f"{invite[3]} you are invited to dinner!")
print(f"{invite[4]} you are invited to dinner!")
print(f"{invite[5]} you are invited to dinner!")


