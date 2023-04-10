#How the input() Functions works

# the input)= function pauses your program and waits fo the user to enter some text.

message = input("Tell me something , and I will repeat it back to you: ")
print(message)

#Note: Sublime Text and many other editors don't run programs that prompt the user for input. You can use these editors to write programs that prompt for input, but you'll need to run these programs from a terminal.

#Letting the user choose when to quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program: "

message = ""

while message != 'quit':
    message = input(prompt)
    #This program works well, except that it prints the word 'quit' as if it were an actual message a simple if test fices this:
    #now the porgram makes a quick check before displaying the message and only prints the message if it does not match the quit value:
    print(message)

#Using a flag


