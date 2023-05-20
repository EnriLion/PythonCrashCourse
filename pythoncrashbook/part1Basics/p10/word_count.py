#Working with Multiple Files
##Count_words() it's a good aproximation it will be easier to run the analysis for multiple books:
def count_words(filename):
    """Count the approximate number of words in a file."""#1
    try:
        with open(filename, encoding='utf-8') as f:
            contents= f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist")
        #-Failing Silently-
        #To make a program file silently you write a tri block as usual but for that reason Python has a pass statement that tells it to do nothing in a blocl:
        #Also acts as a placeholder it's a reminder that you're choosing to do nothing at a specific in your program's execution.
        pass
        
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
# filename = 'alice.txt'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# count_words(filename)
for filename in filenames:
    count_words(filename)
#1)It's a good habit keep coments up to date when you are modifying a program, so we changed the comment to a doct string and reworded it slightly

#Example:
#The mission one or tho has no effect on the rest of the program's execution:
# The file alice.txt has bout 29465 words
# Sorry, the file siddharta.txt does not esit
# The file moby_dick.txt has bout 215830 words
# The file little_women.txt has bout 189079 words
#The file if we don't have the traceback never run the other books contents

#Deciding which erros to report
##How much to share with users when things go wrong: it's up to you to decide how much information to share. Well-written propely tested code is not very prone to internal errors(existence of a file, ability of network connection, there is possibility of an exception being rased) a little experience will help you know
