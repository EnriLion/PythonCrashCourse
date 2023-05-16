with open('learning_python.txt') as file_object:
    content = file_object.read()

#replacing Python with another language
replace = content.replace('Python', 'C')
print(replace)
