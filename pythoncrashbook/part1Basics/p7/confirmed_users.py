##Using a while Loop with Lists and Dictionaries
#Moving Items from One List to Another

#Consider a list of newly registered but unverified website. After we verify these users, how can we move them to a separate list of confimerd users? One way woule be to sue a while loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users. Here's what that code might look like:

#Start with users that need to be verfied,
#and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']#begin with a list of unconfirmed users
confirmed_users = []

#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.

while unconfirmed_users:#runs as the list is empty
    current_user = unconfirmed_users.pop()#

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users.

print(f"Verifying user: {current_user.title()}")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

