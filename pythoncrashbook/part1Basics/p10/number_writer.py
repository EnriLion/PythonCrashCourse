#Storing Data

#Maybe you want to store preferences in a game or provide data for visualization whatever the focus of your program is you'll store the information in data structures as lists and dictionries. When users close a program, you'll almost always want to save the information they entered. A simple way involves storing our data in json modules

#The json modules allows you to dump simple Python data structures into a file and load the data.

#Note: The JSON(JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python.

#Using json.dump() and json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'#we choose a filenam in which to store the list of numbers
with open(filename, 'w') as f:#We open the file in write mode, which allows json to writ the data to the file
    json.dump(numbers, f)#we use the json.dump() function to store the list numbers in the file numbers.json
