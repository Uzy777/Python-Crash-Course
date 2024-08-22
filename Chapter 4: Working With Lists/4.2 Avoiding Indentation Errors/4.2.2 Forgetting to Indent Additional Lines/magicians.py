# Forgetting to Indent Additional Lines

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I cant't wait to see your next trick, {magician.title()}.\n")

# No error but the second print is only executed once has is no longer in the for loop