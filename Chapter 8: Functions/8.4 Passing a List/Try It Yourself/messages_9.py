# 8-9. Messages:    Make a list containing a series of short text messages. Pass the list to a function called show_messages, which prints each text message.

def show_messages(msg):
    """Print each text message"""
    for message in msg:
        print(message)

short_text_msg = ['Thinking of you always.', 'Dinner at our place?', 'Cant wait to meet!', 'Miss your smiling face.', 'Youre my happy place.']
show_messages(short_text_msg)
