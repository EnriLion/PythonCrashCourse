#Exceptions

##When you use try-except blocks, your program will continue running even if things start to go wrong(Instead of tracebaks we could handle friendly error messages that the user could read)

#Handling the ZeroDivisonError Exception

# print(5/0) Of course this input will tell python that is wrong the division by zero(is undefined) but whit python we could use tracebacks if that happened again

#Using try-except Blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
