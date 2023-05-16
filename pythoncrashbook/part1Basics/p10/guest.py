filename = 'guest.txt'

name = input("Give me your name: ")
with open(filename, 'w') as file_object:
    file_object.write(f"{name.title()}")
