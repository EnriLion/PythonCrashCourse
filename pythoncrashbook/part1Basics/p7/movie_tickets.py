prompt = "\nWhat is your age?"
prompt +="\nAnd I will give you the charge :"


while True:
    message = int(input(prompt))
    if message <= 3:
        charge = "free"  
        break
    elif message > 3 and message <= 12:
        charge = 10 
        break
    elif message > 12:
        charge = 15
        break
print(f"\nThe cost of the movie is {charge} ")
        
