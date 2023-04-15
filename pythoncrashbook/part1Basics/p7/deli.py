
unconfirmed_sandwiches = ['chicken', 'egg', 'seafood', 'grilled chesse']#begin with a list of unconfirmed users
finished_sandwiches = list()

#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.

while unconfirmed_sandwiches:#runs as the list is empty
    current_sandwich = unconfirmed_sandwiches.pop()# runs as long as the list unconfirmed is not empty with the pop() funct removes unverfied users one at a time from the of  unformed_users
    print(f"I made your  {current_sandwich.title()} Sandwich")
    finished_sandwiches.append(current_sandwich)


#Display all confirmed users.

print(f"The following sandwiches have been confirmed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

