#Classic way for loop

numbers = list()

for number in  range(1,11):
    numbers.append(number**3)
print(numbers)

#List comprehension
print("\n")
numbers = [number**3 for number in range(1,11)]
print(numbers)
