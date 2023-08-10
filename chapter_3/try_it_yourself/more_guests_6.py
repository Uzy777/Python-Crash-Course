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


