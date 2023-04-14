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
print("\n")

        
#Use an active variable to control how lobg the loop runs
print("\n")

flag = True

while flag:
    message = input(prompt)
    advise= f"Adding the topping({message}) to your pizza"
    print(advise)
    if message == "quit":
         flag = False
#Use a break statement to exit the loop when the user enters a quit



print("\n")

while flag:
    message = input(prompt)
    advise= f"Adding the topping({message}) to your pizza"
    print(advise)
    if message == "quit":
        break
