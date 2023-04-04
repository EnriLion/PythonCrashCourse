current_users = ['roberto', 'jordan', 'michael']

new_users = ['jordan', 'mikey', 'enrique']

for new_user in new_users:
    if new_user in current_users:
        print(f"The {new_user} is not available, enter a new username")
    else:
        print(f"The {new_user} is available")

print("\nFinished making the status of the current users.")


