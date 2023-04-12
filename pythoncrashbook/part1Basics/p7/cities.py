#Using break to exit a loop

#Consider a program that asks the user about placea they've visited  we could break the loop as soon as the user enter quit to break the loop


prompt = "\nPlease enter the name of the city you have visited"
prompt +="\n(Enter 'quit' when you are finished: )"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")



