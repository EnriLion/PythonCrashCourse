responses = {}

switch = True

visit = "If you could visit one place in the world, where would you go?: "
exit = "Would you like to let another person respond? (yes/no): "
while switch:
    name = input("\nWhat is your name?: ")
    response = input(visit)

    responses[name] = response

    repeat = input(exit)
    if repeat == 'no':
        switch = False

#Polling si complete. Show the results.
print("\n--- Poll Results --")
for name,response in responses.items():
    print(f"{name} would like to travel {response}.")
