import json

filename = 'numbers.json'

with open(filename) as f:#we open it in read mode
   numbers = json.load(f)#we use the json.load() function to load the infomration stored in numbers.json and we assing it to the variable numbers and finally we printed

print(numbers)

#This is the simple way to share data betwen two programs.
