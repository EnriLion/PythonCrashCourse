#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #We make a copy of the list by aking for a slice 

print("My favorite foods are: ")
print(my_foods)


print("\nMy favorite foods are: ")
print(friend_foods)

#We have separate lists

my_foods.append('cannoli')

friend_foods.append('ice cream')

#For that reasons there are two differents list:


print("\nMy favorite foods are: ")
print(friend_foods)


print("\nMy favorite foods are: ")
print(my_foods)

##4-12 More loops

for fods in my_foods:
    print("\n",f"This are my favorite foods {fods.title()}")


for myfrifoods in friend_foods:
    print("\n",f"This are my friends foods {myfrifoods.title()}")


##What happened  if we are trying to copy a list without using a slice:

#This doesn't work:
friends_foods = my_foods

#Instead of beign equall to the previous will be associate both variables point to the same list as a result when we add 'cannoli; to my_foods it will also appear in friends_foods. Likewise 'icrecream' will appear in both lists, even though it appears to be added only to friends_foods.



