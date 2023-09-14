current_users = ["bob", "dave", "rachel", "claire", "frank"]
new_users = ["bill", "hank", "frank", "rachel", "stuart"]

upper_current_users = [current.upper() for current in current_users]

for current in current_users:
    if current in new_users:
        print(f"You will need to enter a new username as {current.title()} is already in use.")
    else:
        print(f"The username {current.title()} is available to use.")