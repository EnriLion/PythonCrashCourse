#The easiest way

prompt = "\nGive me each topling to our pizza: "
prompt +="\nEnter 'quit' to end the program: "

message = ""


while message != "quit":
    message = input(prompt)
    if message != "quit":
        advise= f"Adding the topping({message}) to your pizza"
        print(advise)


#Use a conditional test in the while statement to stop the loop

#Use an active variable to control how lobg the loop runs
print("\n")

flag = True

while flag:
    message = input(prompt)
    advise= f"Adding the topping({message}) to your pizza"
    print(advise)
    if message == "quit":
         flag = False

