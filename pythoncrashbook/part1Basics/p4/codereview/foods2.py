#Copying a list
My_foods = ['pizza', 'falafel', 'carrot cake']
Friend_foods = My_foods[:] #We make a copy of the list by aking for a slice 

print("My favorite foods are: ")
print(My_foods)


print("\nMy favorite foods are: ")
print(Friend_foods)

#We have separate lists

My_foods.append('cannoli')

Friend_foods.append('ice cream')

#For that reasons there are two differents list:


print("\nMy favorite foods are: ")
print(friend_foods)


print("\nMy favorite foods are: ")
print(My_foods)

##What happened  if we are trying to copy a list without using a slice:

#This doesn't work:
Friends_foods = My_foods

#Instead of beign equall to the previous will be associate both variables point to the same list as a result when we add 'cannoli; to My_foods it will also appear in Friends_foods. Likewise 'icrecream' will appear in both lists, even though it appears to be added only to Friends_foods.



