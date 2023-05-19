#Exceptions

##When you use try-except blocks, your program will continue running even if things start to go wrong(Instead of tracebaks we could handle friendly error messages that the user could read)

#Handling the ZeroDivisonError Exception

# print(5/0) Of course this input will tell python that is wrong the division by zero(is undefined) but whit python we could use tracebacks if that happened again

#Using try-except Blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#Usin Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    # answer = int(first_number) / int(second_number)
    # print(answer)
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


#if we print the 5 and 0 again will given us a trace back

