message_text = ['howdy', 'lol', 'bye', 'hehe', 'lmao']
# completed_messages = []
sent_messages = []
def send_messages(message_text, sent_messages):
    """
    Send the messages and delete the old ones
    """
    while message_text:
       current_message = message_text.pop()
       print(f"Message: {current_message}")
       sent_messages.append(current_message)

# def sent_messages(completed_messages):
#     """
#     Moving each message to a new list
#     """
#     print("\nThe following messages were printed:")
#     for completed_message in completed_messages:
#         print(completed_message)

send_messages(message_text[:], sent_messages)
# sent_messages(completed_messages)
print(message_text)
# print(completed_messages)
print(sent_messages)
