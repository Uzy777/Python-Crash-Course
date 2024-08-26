# 8-3. T-Shirt:     Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should
#                   print a sentence summarising the size of the shirt and the message printed on it.
#                   Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(shirt_size, shirt_message):
    print(f"You have selected {shirt_size.upper()} and a the following message '{shirt_message}'")

make_shirt('M', 'I am a strong man!')
make_shirt(shirt_size='M', shirt_message='I am a strong man!')
