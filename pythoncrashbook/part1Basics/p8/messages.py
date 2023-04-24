def show_messages(messages):
    """ Print a simple text message"""
    for message in messages:
        grt = f" Message: {message.title()}"
        print(grt)

message_text = ['howdy', 'lol', 'bye', 'hehe', 'lmao']
show_messages(message_text)

