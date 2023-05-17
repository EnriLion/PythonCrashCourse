filename = 'programming_poll.txt'
flag = True
while flag:
    print('Press q or q to quit!!')
    poll = input("Why you like programming?: ")
    if poll == 'q' or poll == 'Q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(f"{poll.title()}\n")
