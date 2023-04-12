#The easiest way

prompt = "\nGive me each topling to our pizza: "
prompt +="\nEnter 'quit' to end the program: "

message = ""


while message != "quit":
    message = input(prompt)
    if message != "quit":
        advise= f"Adding the topping({message}) to your pizza"
        print(advise)



