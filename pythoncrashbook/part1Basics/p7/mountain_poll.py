#Filling a dictionary with user input

responses = {}

# Set a flag to indicate that polling is active

polling_active = True

while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")

    #Store the response in the dictionary.
    responses[name] = response # the input is stored in the responses dictionary

    #Find out if anyone esle is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)")# if enters yes or whether input except no will be repeat the loop
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n--Poll Results --") #displays the results of the poll
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


