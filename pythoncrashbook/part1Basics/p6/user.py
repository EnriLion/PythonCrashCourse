#Looping through all key-value pairs

user_0 = {
        'username': 'efermi',
        'first' : 'enrico',
        'last': 'fermi',
        }
for key, value in user_0.items():# Write through the loop we need two variable which are the key and value pair and lopp through the itmes but in abbreviations could be for k, v in user_0.items()
    print(f"\nKey: {key}") #We print the key 
    print(f"\nValue: {value}")#We print the value


