#The modulo operator doesn't tell you how many times one number fits into another, you can use this fact to determine if a number is even or odd:

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#Even numbers are always divisible by two, so if the module of a number and two is zero ( here if number % 2 == 0) the number is even. Otherwise, it's odd.
