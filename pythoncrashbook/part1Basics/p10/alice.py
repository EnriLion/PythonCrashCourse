#Handling the FileNotFoundError Exception

#The file doesn't exist and will give us a traceback.

filename = 'alice.txt' 

with open(filename, encoding='utf-8') as f:
    contents= f.read()

#If we run it:
# Traceback (most recent call last):
#   File "/data/data/com.termux/files/home/PythonCrashCourse/pythoncrashbook/part1Basics/p10/alice.py", line 7, in <module>
#     with open(filename, encoding='utf-8') as f:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
