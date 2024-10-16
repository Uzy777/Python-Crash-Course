# 8-10. Sending Messages:   Start with a copy of your program from Exercise 8-9.
#                           Write a function called send_messages() that prints each text message and moves each message
#                           to a new list called sent_messages as it's printed. After calling the function, pritn both of your 
#                           lists to make sure the messages were moved correctly.

def send_messages(short_text_msg, sent_messages):
    """Print each text message"""
    while short_text_msg:
        current_message = short_text_msg.pop()
        print(current_message)
        sent_messages.append(current_message)

short_text_msg = ['Thinking of you always.', 'Dinner at our place?', 'Cant wait to meet!', 'Miss your smiling face.', 'Youre my happy place.']
sent_messages = []

send_messages(short_text_msg, sent_messages)

print("\nMessage")
print(short_text_msg)
print("\nSENT Message")
print(sent_messages)
