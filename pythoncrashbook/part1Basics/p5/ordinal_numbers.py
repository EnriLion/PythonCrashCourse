numbers = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
space = ' '
for number in numbers:
    if number == 1:
        number = "1st" + space
    elif number == 2:
        number = "2nd" + space
    elif number == 3:
        number = "3rd" + space
    elif number <= 9:
        number = str(number) + "th" + space
    else:
        print("We don't find the name sorry")
    # output = output + number = output += number
    print(number, end= ' ')
print()

    
    

