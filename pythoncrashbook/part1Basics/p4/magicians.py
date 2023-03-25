magicians = ['alice', 'david', 'carolina']

for magician in magicians: 
#    print(magician)

##Doing More Work Within a for loop

    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

##Doing something after a for loop

print("Thank you everyone. That was a great magic show!")

##The reason is what is not printing a lot of times is because is not intended that's means is not inside the loop


#Tehcnically the variable magician is assignin the value of each list in the variable(magician) and printing until the end of the length of the list().

#The line tells Python to pull a name from the list magicians and associate it with the variable magician and to print each list of the variable

#Take a look a good way to understand a list of itmes with these examples:


print("\nCats")

cats = ['persian', 'british', 'abyssinian']

for cat in cats:
    print("\n",cat)


print("\nDogs")

dogs = ['malamute', 'american', 'terrier']

for dog in dogs:
    print("\n",dog)

print("\nItems")

items = ['cocacola', 'pepsicola', 'redcola']

for item in items:
    print("\n",item)

#These naming conventions can help you followe the action bein gdone on each time within a for loop. Using sinfular and plural names can help you idenitfy where a section of code is working with a single elemtn from the list on the entire list.

#We can also write as many lines of code as we like in the for loop. Every indented line following the line for magician in magicians in considered "inside the loop" and each indented line is executed once for each value in the list.

#If you don't ident will make python  make an output call IndentatinoError: expected an indented block
