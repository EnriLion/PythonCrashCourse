##Numerical Comparisons
#Make a comparisons if two numbers are not equla:

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

#You can include various mathematicla comparions in your conditional statements as well such as  less than, equal to, greater than, greatear than and equal to:

Age = 19

Test_age = Age < 21

print("\n",Test_age)


Test_age = Age <= 21

print("\n",Test_age)


Test_age = Age > 21

print("\n",Test_age)

Test_age = Age >= 21

print("\n",Test_age)

##Checking Multiple Conditions

#The keywords "and" and "or" can help you in these sitations when you want two conditions to be True to take an action

#Using and to Check Multiple Conditions

#To check whether two conditions are both True siumultaneously us eht ekeyword "and" to cobine the two conditional tests

#You can check where two people are both over 21 using the follwin test:

age_0 = 22

age_1 = 18

comparison = age_0 >= 21 and age_1 >= 21 #print false because one of the variables give the result of false 

print('\n', comparison)


age_1 = 22

comparison = age_0 >= 21 and age_1 >= 21 # if both of them give as result will be True

print('\n', comparison)

#To improve readiblity you can do this:



comparison = (age_0 >= 21) and (age_1 >= 21)

print('\n', comparison)

##Using or to Check Multiple Conditions

age_0 = 22

age_1 = 18


comparison = age_0 >= 21 or age_1 >= 21 #If one of them are true the result will be True 

print('\n', comparison)


age_0 = 18


comparison = age_0 >= 21 or age_1 >= 21 #If both are greater than 21 will be true otherwise(both of them right now) the result will False


print('\n', comparison)

#Checking whether a value is in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']

What_toppings = 'mushrooms' in requested_toppings # the variable 'in' help us to to see if a string is in a list or array


print('\n', What_toppings)


What_toppings = 'pepperoni' in requested_toppings 


print('\n', What_toppings)


