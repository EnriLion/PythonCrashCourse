

prompt = "\nWhat is your age?"
prompt +="\nAnd I will give you the charge"


flag = True

while flag:
    message = int() 
    message = input(prompt)
    if message == 3:
        print("Your ticket is free")
        flag = False
    if message == 12:
        print("Your ticket is $10")
        flag = False

   
