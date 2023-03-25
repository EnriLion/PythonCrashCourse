##Using range() to make a list of numbers

squares = [] #Variable of a list

for value in range(1, 11):#We tell pythonn to loop through each avlue from 1 to 10 using the range() function
    square = value **2# the square value is assigned the variable value to the second power able in the square
    squares.append(square)# append the list square to the list squares 

print(squares)

#We can create 10 square numbers ( that is the square of each integer from 1 thoguh 10) and in Python two asteriks(**) represent exponents.

##Simple statistics with a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("\n")
print(min(digits))
print("\n")
print(max(digits))
print("\n")
print(sum(digits))

#List comprehensions

#Works like a loop and the below code presents the same element as above using the square numbers

print("\n")
squares = [value**2 for value in range(1, 11)]
print(squares)


