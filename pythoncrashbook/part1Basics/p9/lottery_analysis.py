from random import choice, randint
my_ticket= (15, 6, 8, 9, 11, 4, 3, 5, 20, 12)
for x in range(1,20):
    for my_tickets in my_ticket:
        m = my_tickets
        if x == m:
            print(f"You won the lottery at your {x} attempt")
        break


