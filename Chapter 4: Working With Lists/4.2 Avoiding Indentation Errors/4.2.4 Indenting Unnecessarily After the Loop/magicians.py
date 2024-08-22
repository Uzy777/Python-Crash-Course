# Intending Unnecessarily After the Loop

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")

# Because the last line is indented, it's printed once for each person in the list.