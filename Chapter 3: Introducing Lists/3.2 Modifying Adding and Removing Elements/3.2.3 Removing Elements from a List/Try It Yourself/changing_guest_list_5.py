# 3-5. Changing Guest List:     You just heard that one of your guests can't make the dinner,
#                               so you need to send out a new set of invitations. You'll have to think of someone else to invite.
#
#                               - Start with your program from Exercise 3-4. Add a 'print()' call at the end of your program,
#                               stating the name of the guest who can't make it.
#                               - Modify your list, replacing the name of the guest who can't make it with the name of 
#                               the new person your are inviting.abs
#                               - Print a second set of invitation messages, one for each person who is still in your list.

invite = ["Ali", "Mike", "Khabib"]
print(f"{invite[0]} you are invited to dinner!")
print(f"{invite[1]} you are invited to dinner!")
print(f"{invite[2]} you are invited to dinner!")

print(f"Sadly our guest {invite[1]} can not make it for dinner.")

invite[1] = "Beth"
print(f"{invite[0]} you are invited to dinner!")
print(f"{invite[1]} you are invited to dinner!")
print(f"{invite[2]} you are invited to dinner!")