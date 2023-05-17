filename = 'guest_book.txt'
while True:
    print("Press q or q to quit!!")
    name = input("Give me your name: ")
    if name == 'q' or name == 'Q':
        break
    with open(filename, 'a') as file_object:
        welcome = f"Welcome {name.title()}\n"
        file_object.write(welcome)
    print(welcome)
