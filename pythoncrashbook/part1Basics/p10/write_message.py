#Writing to a File
##You can examine the output after a program finishes running and share it, also write programs that read the text back into memory and work again later

#Writing to an Empty File
## To write text we need to call open() with a second argument:

filename = 'programming.txt'

# with open(filename, 'w') as file_object:#the open function has two arguments ( the first(name of the file) and the second('w') tells Python we ant to open the file in write mode also there are readmode('I'), append mode ('a') or a mode that allows you to read and write to the file ('I+'); by defualt opens the file in read-only mode by default
with open(filename, 'a') as file_object:
    # file_object.write("I love programming.\n")

#Note: Python can only write strings to a text files. 

##Writing Multiple Lines
    # file_object.write("I love creating new games.\n")

#If we open the file manually you'll se the two lines squished...
#I love programing.I love creating new games

#Including newlines in your calls to write() makes each string appear on its own line:

#We can also use spaces, thab characters, and blank lines to format your output,just as you've been doing with therminal-based output

##Appending to a File
#Python only append content does not erase it.

    file_object.write("I also love finding meaning in the large datasets.\n")
    file_object.write("I love creating apps that can run in a broswer.\n")

