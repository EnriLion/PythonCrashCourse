#The if-elif-else Chain

##Example  a musement park that charges different rates for different age groups:

# Admission for anuone under age 4 is free

# Admision for anyone between the ages of 4 and 18 is $25

# Admission for anuone age 18 or older is $40

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


#We could set just the price inside the if-elif-else chain

print("\n")


age = 12


if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")

#This solution is better because produce the same output as the previous example but the purpose of the if-elif-else chain is narrower and this code is easy to revisit and modify than the original is better change print() call than three to separate print() calls

#Using Multiple elif Blocks

print("\n")



age = 12


if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20 # in the case people is older than 65( the discount for seniors)

print(f"Your admission cost is ${price}")

print("\n")

#Omitting the else block

## Python does not require a neccesity of else at the end and sometimes elif statement catches the specific condition of interest:

age = 12


if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: # in this case the greater than and equal than 65 will be set the price = 20
    price = 20 

print(f"Your admission cost is ${price}")
