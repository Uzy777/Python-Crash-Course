# 8-11. Archived Messages:  Start with your work from Exercise 8-10. Call the function send_messages() with a 
#                           copy of the list of messages. After calling the function, print both of your
#                           lists to show that the original list has retained its messages.


def send_messages(short_text_msg, sent_messages):
    """Print each text message"""
    while short_text_msg:
        current_message = short_text_msg.pop()
        print(current_message)
        sent_messages.append(current_message)


short_text_msg = ['Thinking of you always.', 'Dinner at our place?', 'Cant wait to meet!', 'Miss your smiling face.', 'Youre my happy place.']
sent_messages = []

send_messages(short_text_msg[:], sent_messages)

print("\nMessage")
print(short_text_msg)
print("\nSENT Message")
print(sent_messages)