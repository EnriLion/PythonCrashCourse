#Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:#if the modulr is 0 that means that is dvisible by two
        continue

    print(current_number)

#We can use continue to return to the beginning of the loop

#Avoiding infinite loops
print("\n")

x = 1

while x <= 5:
    print(x)
        
