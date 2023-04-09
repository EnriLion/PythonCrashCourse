#How do you use the int() function in an actual program? Consider a program that determines whether people are tall enough to ride a roller coaster:

height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou' re tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")
    
print("\n")
#The modulo operator

#A useful tool for workin with numerical information i shte modulo operator(%) which divides one number by another number and returns the remainder:
x = 4

y = 3

comparison = float()

comparison = x % y

print(comparison)

