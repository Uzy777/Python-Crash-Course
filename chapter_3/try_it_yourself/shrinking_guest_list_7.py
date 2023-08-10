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

print("\nI am afraid that there is only space for two guests now as the tables are not going to arrive in time!\n")

invite_pop = invite.pop(0)
print(f"I am sorry {invite_pop} but you are no longer invited to dinner!")

invite_pop = invite.pop(2)
print(f"I am sorry {invite_pop} but you are no longer invited to dinner!")

invite_pop = invite.pop(3)
print(f"I am sorry {invite_pop} but you are no longer invited to dinner!")


invite_pop = invite.pop(1)
print(f"I am sorry {invite_pop} but you are no longer invited to dinner!")

print(f"\nSorry for the issues caused {invite[0]} and {invite[1]} you are still invited to dinner!\n")

del invite[0]
del invite[0]

print(invite)


