#Handling the FileNotFoundError Exception

#The file doesn't exist and will give us a traceback.

filename = 'alice.txt' 


# with open(filename, encoding='utf-8') as f:
#     contents= f.read()

#If we run it:
# Traceback (most recent call last):
#   File "/data/data/com.termux/files/home/PythonCrashCourse/pythoncrashbook/part1Basics/p10/alice.py", line 7, in <module>
#     with open(filename, encoding='utf-8') as f:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents= f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
#Analylizing text
else:
    #split() method separates a string into parts 
    #count the aproximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    #If a fyle exist will aproximat the word numbers of the file
