#Working with a File's Contents

# filename = 'pi_digits.txt'
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''#we create a variable, pi_string to hold the digist of pi
for line in lines:#we create a loops that adds each line of digits to pi_string and removes the newline character from each line
    # pi_string += line.rstrip()
    pi_string += line.strip()#  pistring_contains the whitespace that was on the left side of the digits in each line, but we van use strip to get rid of it and now the length of the string is 36 instead of 32 because it also include leading 3 and a decimal point

# print(pi_string)#we print this string
# print(len(pi_string)) #we prin the string and how long the string is

print(f"{pi_string[:52]}...")
print(len(pi_string)) 

#Large Files: One Million Digits
#output of len:
#10002 instead of 102 but we only have 102 characters not 10002 chracters as the example
