
with open('learning_python.txt') as file_object: 
    contents = file_object.read()
       #printin 3 times in a row
        # print(contents)
        # print(contents)
        # print(contents)
        #the easiest way 3 times with loop
    # for i in range(0,3):
    #     print(contents)
cont_string = ''
for content in contents:
    cont_string += content.strip()

# print(cont_string)

#Is anything inside in the string

inthere= input("Enter your birthday, in the form mmddyy: ")#Prompt the user birthday
if  inthere in cont_string:#We check if that string is in pi_string:
    print("Your string looks like is in the file.")
else:
    print("Your string doesn not appear in the file.")

