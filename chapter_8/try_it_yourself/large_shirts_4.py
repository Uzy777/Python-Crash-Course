# 8-4. Large Shirts:    Modify the make_shirt() function so that shirts are
#                       large by default with a message that reads I love Python.
#                       Make a large shirt and a medium shirt with the default message,
#                       and a shirt of any size with a different message.


def make_shirt(shirt_size='L', shirt_message='I love Python'):
    print(f"You have selected {shirt_size.upper()} and a the following message '{shirt_message}'")

make_shirt()
make_shirt(shirt_size='M')
make_shirt(shirt_size='XS', shirt_message='I am a strong man!')