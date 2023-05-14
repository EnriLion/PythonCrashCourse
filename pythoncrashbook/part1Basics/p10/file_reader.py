#Progtam that opens this file, reads it, and prints the contents of the file to the screen:

# with open('pi_digits.txt') as file_object: 
#     contents = file_object.read()
#     print(contents.rstrip())# remove the extra blank line, we can use rstrip() function and print it.

# print(contents)

#Program that opens the file, reads it and prints the contents of the file

#The open() function prints the contents and need to open the file to access it. and python looks for this file in the directory where the program that's currently being executed is stored and python looks for pi_digits.txt and the open() returns an object representing the file and python assing this object to file_object 

#Notice that we have the open() and the close() tunction( but python will figure that for you and will close it automatically when the with block finishes execution

#File Paths

##When you pass a simple filenmae(pi_figits.txt) to the open() function; looks in the directory where the file that's currently being executed

#Sometimes, dependeing the file we want to open in the same directory as our program file, for example, you mifht store your program files in a folder callderpython_work inside python_work you might have another folder called text_files to distinghis our program:

#with open('text_files/filename.txt') as file_object:

#Note:Windows systems use backlash (\)( but we can still use slashes on our code)

#Absolutes and relative paths

#ex file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
#with open(file_path_ as file_object:

#Note: If you try to use backlashes you'll get an error because the backlas is used to escape characters in strings. For example in the path "C:\path\to\file.txt' the sequence \t is interpreted as a tbal you can escape each one in the path "C:\\path\to\\file.txt"

#Reading Line by Line

#You might want to read through a file of weather data dn work with any line that includes the word sunny in the description of that day's weather. In a news report, you might look for any line with the tag <headline> and rewrite that line with a specific kind of formatting.
#You can use a for loop on the file object to examine each line from a file one at a time:

# filename = 'pi_digits.txt'#We assing the name of the file we're reading from the variable filename

# with open(filename) as file_object: #We could easily swap out for the name of another file you want to work with after we call open() an object representing the file and its contents is assigned to the variable file_object. and we again use the with syntax to let Python to p[em am d close the file properly
#     for line in file_object:# we loopp through each lin in the file by looping over the file object.
#         # print(line)
#         print(line.rstrip())

#Making a List of lines from a file

#Wehn you use with, the file object returned by open() is only available inside the with block that contains it. If you want to retain access to a file's contents outside the with block, you can store the file's lines in a list inside the block and then work with that list. You can process parts of the file immediately and postpone some precessing for alter in the program.
#The next lines of pi_digits.txt in a list inside the with block and then print s the lines outside the with block:


filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
